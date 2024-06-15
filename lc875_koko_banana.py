from typing import List
from math import ceil
class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # binary search for min k
    l, r = 1, max(piles) # O(n)
    while l<r: # O(logn)
      k = (l+r)//2
      hh = sum([ceil(pile/k) for pile in piles]) # O(n)
      if hh <= h: # koko succeeds, but can she succeed slower?
        r = k
      else: # hh > h; koko needs to eat faster
        l = k+1
    return l