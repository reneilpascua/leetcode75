from typing import List

class Solution:
  def maxProfit_dfs(self, prices: List[int], fee: int) -> int:
    # brute force solution... explores every option on each day
    # without memoization

    maxp = 0
    times_called = 0
    def dfs(hold, profit, plist):
      nonlocal maxp, times_called
      times_called += 1
      if not plist:
        maxp = max(maxp, profit)
        return
      
      p0 = plist[0]
      if hold is None:
        # buy on this day, dfs go next
        dfs(p0, profit - p0, plist[1:])
      elif p0 < hold:
        # was holding something, but realized the next day is cheaper
        dfs(p0, profit + hold - p0, plist[1:])
      else: # p0 >= hold
        # explore decision to not sell
        dfs(hold, profit, plist[1:])
        # explore decision to sell
        sale = p0 - fee
        if sale > hold:
          dfs(None, profit+sale, plist[1:])

    dfs(None, 0, prices+[0])
    print('days: ',len(prices),', fee:',fee,', dfs called',times_called,'times')
    return maxp

if __name__ == '__main__':
  ex1 = ([1,4,3,6,1], 2)
  ex2 = ([1,4,3,6,1], 1)
  ex3 = ([1,4,3,6,1], 0)
  ex4 = ([1,3,2,8,4,9], 2)
  print(Solution().maxProfit(*ex3))