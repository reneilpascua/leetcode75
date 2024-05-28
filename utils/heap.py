from typing import List

class Heap:
    """
    Tree-like data structure that maximizes the root node.
    """
    def __init__(self, maxing_function = None):
        """
        Initializes a heap where the root is "greater than" than its children.
        Use a custom maxing function to define what "greater than" means.
        """
        self.maxing_function = maxing_function if maxing_function else Heap._maxing
        self.heap = []


    def add(self):
        pass
    
    def pop(self):
        pass

    def _heapify(self):
        pass

    @staticmethod
    def generate(list: List, maxing_function = None):
        """
        Generates a heap by iterating through a given list and maxing function.
        """
        h = Heap(maxing_function)

    @staticmethod
    def _maxing(a, b):
        """
        The default maxing function. Makes use of a and b's comparator functions
        and returns True if a is "greater than" b
        """
        return a > b