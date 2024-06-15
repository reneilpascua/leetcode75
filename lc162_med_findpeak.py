from typing import List

class Solution:
  
  # binary search soln
  def findPeakElement(self, nums: List[int]) -> int:
    nums = [float('-inf')] + nums + [float('-inf')]
    
    l, r = 1, len(nums)-2
    while l < r:
      m = (l+r)//2
      # is m a peak?
      if nums[m-1] < nums[m] > nums[m+1]:
        return m-1
      elif nums[m] < nums[m+1]: # uphill to the right
        l = m + 1
      elif nums[m] < nums[m-1]: # uphill to the left
        r = m
    return l-1

  # this is the O(n) soln which ends up beating over 80% ...
  def findPeakElement_n(self, nums: List[int]) -> int:
    nums = [float('-inf')] + nums + [float('-inf')]
    
    i = 0
    while i < len(nums) - 1 and nums[i] < nums[i+1]:
      i += 1
    return i-1  
