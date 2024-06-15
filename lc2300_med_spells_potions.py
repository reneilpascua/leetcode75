from typing import List
import bisect
from math import ceil


class Solution:
  def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    potions.sort()

    # use built-in bisect lib instead of my own binary search
    ans = []
    for spell in spells:
      required_str = ceil(success/spell)
      
      # left-most index i where potions[i] >= required_str
      i = bisect.bisect_left(potions, required_str)
      ans.append(len(potions)-i)

    return ans


  # probably the downfall of this solution is the excessive sorting
  def successfulPairs_0(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    spells = sorted([(spell, i) for i,spell in enumerate(spells)], key = lambda x: -x[0])
    potions.sort()
    # sorting is nlogn and mlogm

    ans = []
    l = 0
    for spell, i in spells:
      # find the first potion that is strong enough. then the rest of
      # the potions will also be strong enough.
      # carry on the minimum (var l) to the next iteration
      required_str = success/spell
      r = len(potions)-1
      while l<r:
        m = (l+r)//2
        if potions[m] >= required_str: # we may have overshot. reduce range from right
          r = m
        else:
          l = m+1
      ans.append(
        (len(potions)-l, i)
        if potions[l] >= required_str else (0,i)
      )
    # the for-loop is O(n), the nested while loop is O(log(m))

    ans.sort(key = lambda x: x[1]) # nlogn
    return [x[0] for x in ans]


if __name__ == '__main__':
  ex1 = (
    [5,1,3],
    [1,2,3,4,5],
    7
  )
  print(Solution().successfulPairs(*ex1))