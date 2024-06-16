from typing import List
class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    if n > 45: return [] # sum of all 1-9 is 45

    # find k unique single-digit numbers that sum to n
    combos = []
    def dfs(nums: List[int], available: List[int], pathsum: int):
      if pathsum > n or len(nums) > k: return
      if pathsum == n and len(nums) == k:
        combos.append(nums)
        return
      for i,a in enumerate(available):
        dfs(nums + [a], available[i+1:], pathsum + a)

    dfs([],[1,2,3,4,5,6,7,8,9], 0)
    return combos