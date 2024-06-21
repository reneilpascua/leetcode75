from typing import List
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    # observation:
    # because we can buy and sell on same day, we can just profit whenever
    # the price is higher (ie. every positive difference)
    # [1,2,3,4,1,3] -> (4-1) + (3-1) = 5
    # OR            -> (2-1) + (3-2) + (4-3) + (3-1) = 5
    profit = 0
    for i in range(1, len(prices)):
      diff = prices[i] - prices[i-1]
      if diff > 0:
        profit += diff
    return profit

  
  def maxProfit_0(self, prices: List[int]) -> int:
    # buy at local min, sell at local max
    N = len(prices)

    profit = 0
    p = prices[0]
    hold = None
    i = 1
    while i < N:
      if hold is None: # look for local min
        if prices[i] > prices[i-1]: # i-1 is a local min
          # print(f'gonna buy on day {i-1} at {prices[i-1]}')
          hold = prices[i-1]
      else: # look for a local max
        if prices[i] < prices[i-1]: # i-1 is a local max
          # print(f'gonna sell on day {i-1} at {prices[i-1]}')
          profit += prices[i-1] - hold
          hold = None
      i += 1
    
    if hold is not None: # then the last element is a local max
      profit += prices[-1] - hold
    return profit

if __name__ == '__main__':
  ex1 = [2,1,2,0,1] # ans 2
  print(Solution().maxProfit(ex1))