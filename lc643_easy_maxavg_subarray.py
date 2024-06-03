from typing import List
class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    # trick here is you dont need to calculate average on each window
    # (this makes the sol O n^2)
    # just add the incoming item and subtract the outcoming
    
    csum = sum(nums[:k])
    msum = csum
    for i in range(1, len(nums)-k+1):
      csum += nums[i+k-1] - nums[i-1]
      msum = max(msum, csum)
    
    return msum/k