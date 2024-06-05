from typing import List
class Solution:
  def longestSubarray(self, nums: List[int]) -> int:
    maxlen = 0
    curlen = 0
    deleted = 0
    l, r = 0, 0
    while r < len(nums):
      if nums[r]: # is 1
        curlen += 1
      else: # is 0
        if not deleted:
          deleted = 1 # allow continuation
        else: # one has already been deleted. move on.
          # find the first 1 after a 0
          while nums[l]:
            l += 1
          else:
            l += 1
          curlen = r - l
      # print(l,r)
      maxlen = max(maxlen, curlen)
      r += 1
    return maxlen if deleted else maxlen-1

if __name__ == '__main__':
  ex1 = [1,1,0,1] # ans 3
  ex2 = [0,1,1,1,0,1,1,0,1] # ans 5
  ex3 = [1,1,1] # ans 2 (need to delete an element)
  print(Solution().longestSubarray(ex1))
  print(Solution().longestSubarray(ex2))
  print(Solution().longestSubarray(ex3))