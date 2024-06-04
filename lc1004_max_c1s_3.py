from typing import List

class Solution:
  def longestOnes(self, nums: List[int], k: int) -> int:
    maxlen = 0
    curlen = 0
    n_zero = 0
    l, r = 0, 0 # edges of the window
    while r < len(nums):
      if nums[r]: # is 1
        curlen += 1
      else: # is 0... turn it into a 1
        if n_zero < k: # free pass
          curlen += 1
          n_zero += 1
        else: # switch from the first flipped-0
          while nums[l] == 1:
            l += 1
          else: # we've found a zero. go past it.
            l += 1
          curlen = r - l + 1
      maxlen = max(maxlen, curlen)
      r += 1
    
    return maxlen
  
if __name__ == '__main__':
  ex1 = ([1,1,1,0,0,0,1,1,1,1,0], 2) # ans 6
  ex2 = ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) # ans 10
  print(Solution().longestOnes(*ex2))