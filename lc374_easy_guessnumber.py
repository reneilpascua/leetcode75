def guess(m: int) -> int:
  pass

class Solution:
  def guessNumber(self, n: int) -> int:
    # guess a number [1,n] by calling guess(x:int)
    l, r = 1, n
    while l < r:
      m = (r+l)//2
      res = guess(m)
      if res == -1:
        r = m-1
      elif res == 1:
        l = m+1
      else:
        return m
    return l
      
