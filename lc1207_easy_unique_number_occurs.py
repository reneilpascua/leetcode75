from typing import List
from collections import defaultdict, Counter
class Solution:
  
  def uniqueOccurrences(
    self,
    arr: List[int]
  ) -> bool:
    c = Counter(arr)
    return len(c.values()) == len(set(c.values()))
  
  def uniqueOccurrences_0(
    self,
    arr: List[int]
  ) -> bool:
    occurrences = defaultdict(int)
    for a in arr:
      occurrences[a] += 1
    
    vals = set()
    for o in occurrences.values():
      if o in vals:
        return False
      else:
        vals.add(o)
    
    return True
  