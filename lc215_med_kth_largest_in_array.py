from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        seen = [float('inf')]
        def add_to_seen(n: int):
            nonlocal seen

            if len(seen) > k+1 and n < seen[-1]:
                return
            i = 0
            l = len(seen)
            while i < l and n < seen[i]:
                i+=1
            seen = seen[:i] + [n] + seen[i:]
        
        for n in nums:
            add_to_seen(n)
        # print(seen)
        return seen[k]

if __name__ == '__main__':
    t = [5,3,7,8,1,2,4]
    print(Solution().findKthLargest(t, 2))