from typing import List
class Solution:
  def maxOperations(self, nums: List[int], k: int) -> int:
    # idea: sort first then traverse from left and right to find sum-k-pairs
    num_ops = 0
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
      lr_sum = nums[l] + nums[r]
      if lr_sum < k:
        l += 1
      elif lr_sum > k:
        r -= 1
      else: # lr_sum == k
        num_ops += 1
        l += 1
        r -= 1
    return num_ops