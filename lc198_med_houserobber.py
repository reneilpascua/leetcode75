from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    # dont want to rob adjacent houses, ie. skip 1 house.
    # question: can it be advantageous to skip 2 houses?
    # ... im inclined to think yes, otherwise you can just return the sum of
    # the list starting from i=0 and i=1
    # ex. [10,1,1,10]
    # there is no advantage to skipping 3 houses though!
    
    # this is like the stairs problem
    if len(nums) == 1: return nums[0]
    self.dp = {-1: 0, 0: nums[0], 1: nums[1]}
    i = 2
    while i < len(nums):
      # skip 1 house: i-2; skip 2 houses: i-3
      self.dp[i] = nums[i] + max(self.dp[i-2], self.dp[i-3])
      i += 1
    
    return max(self.dp[i-1], self.dp[i-2])