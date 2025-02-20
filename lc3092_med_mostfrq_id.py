from typing import List

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        count = dict()
        for i in range(n):
            if nums[i] not in count:
                count[nums[i]] = 0
            count[nums[i]] = max(0, count[nums[i]] + freq[i])
            ans[i] = max(count.values())
        
        return ans

def main():
    pass

if __name__ == '__main__':
    main()