from typing import List
from heapq import heappush, heappop


from utils.performance import timer

class Solution:
    def mostFrequentIDs_0(self, nums: List[int], freq: List[int]) -> List[int]:
        ans = []
        count = dict()

        for num, frq in zip(nums, freq): # O(n)
            if num not in count:
                count[num] = 0
            count[num] = max(0, count[num]+frq)
            ans.append(max(count.values())) # O(n)
        # --> O(n^2)

        return ans # TLE
    
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        ans = []
        count = dict()

        my_heap = [] # default min-heap, uses (-freq, num) for prio queue
        for num, frq in zip(nums, freq): # O(n)
            if num not in count:
                count[num] = 0
            count[num] = max(0, count[num]+frq)
            # push prioritized item into pq (prio = -count)
            heappush(my_heap, (-count[num], num))
            
            # the count-dict keeps track of all frequencies
            # the heap knows the max at one point in time
            # heap's max CAN contain outdated info (ex. if the max was reduced by freq)
            # pop the max(es) from the heap if they don't agree with the corresponding val found in count-dict
            while my_heap[0][0] != -count[ my_heap[0][1] ]:
                heappop(my_heap)

            ans.append(-my_heap[0][0]) # peek and make positive
        # O(n) for the outer loop, and O(1) for the popping since we guarantee at most 2 elements in the heap
        # --> O(n)
        
        return ans

@timer
def main():
    tc1 = ( [2,3,2,1], [3,2,-3,1] )
    tc2 = ( [5,5,3], [2,-2,1] )
    
    s = Solution()
    print(s.mostFrequentIDs(*tc1))
    print(s.mostFrequentIDs(*tc2))

    # use TLE test case from leetcode website
    USE_BIG_TESTCASE = False
    if USE_BIG_TESTCASE:
        from utils.temp_testcase import nums, freq
        s.mostFrequentIDs(nums, freq)

if __name__ == '__main__':
    main()