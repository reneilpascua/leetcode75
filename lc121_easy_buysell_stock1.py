from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    lowest_before = prices[0]
    maxp = 0
    for p in prices:
      if p < lowest_before:
        lowest_before = p
      else:
        maxp = max(maxp, p - lowest_before)
    return maxp