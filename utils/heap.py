from typing import List

def _heapify(heap: List[int], i):
  """
  ensures the tree at node i maintains max heap property.
  proper usage requires heapification upwards from bottom. O(logn)
  """
  
  # indices
  N = len(heap)
  max_index = i
  l = 2*i + 1
  r = 2*i + 2

  if l < N and heap[max_index] < heap[l]:
    max_index = l
  if r < N and heap[max_index] < heap[r]:
    max_index = r
  if max_index != i: # ie. swap, and heapify down
    heap[i], heap[max_index] = heap[max_index], heap[i]
    # heapify the affected sub-tree
    _heapify(heap, max_index)

def create_heap(arr: List[int]):
  """modifies a given array to become a max heap. O(nlogn)"""

  # heapify bottom-up, starting from the last non-leaf node
  N = len(arr)
  last_i = ((N-1)-1)//2 # parent of the last element

  for i in range(last_i, -1, -1):
    _heapify(arr, i)

if __name__ == '__main__':
  arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
  create_heap(arr)
  print(arr)


# class Heap:
#     """
#     Tree-like data structure that maximizes the root node.
#     """
#     def __init__(self, maxing_function = None):
#         """
#         Initializes a heap where the root is "greater than" than its children.
#         Use a custom maxing function to define what "greater than" means.
#         """
#         self.maxing_function = maxing_function if maxing_function else Heap._maxing
#         self.heap = []


#     def add(self):
#         pass
    
#     def pop(self):
#         pass

#     def _heapify(self):
#         pass

#     @staticmethod
#     def generate(list: List, maxing_function = None):
#         """
#         Generates a heap by iterating through a given list and maxing function.
#         """
#         h = Heap(maxing_function)

#     @staticmethod
#     def _maxing(a, b):
#         """
#         The default maxing function. Makes use of a and b's comparator functions
#         and returns True if a is "greater than" b
#         """
#         return a > b