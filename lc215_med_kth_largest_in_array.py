from typing import List
from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sort (O(nlogn)) and then go to the -kth index (O(1))
        # nums.sort()
        # return nums[-k] # O(nlogn)

        # heapify (O(n)) and then pop k-1 times (O(klogn))
        h = [-n for n in nums] # negative to make max heap
        heapify(h)
        for _ in range(k-1):
            heappop(h)
        
        return -h[0] # O(klogn) < O(n) < O(nlogn) assuming k << n

if __name__ == '__main__':
    t = [5,3,7,8,1,2,4]
    print(Solution().findKthLargest(t, 2))