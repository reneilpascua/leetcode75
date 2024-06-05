from collections import Counter
class Solution:
  def closeStrings(self, word1: str, word2: str) -> bool:
    # trick here is that you don't need to know
    # which operations nor how many -- just return whether it's possible

    # op 1: swap chars
    # op 2: transform every instance of a char to another existing char and
    #       do the same to the other char.

    # diff length?
    if len(word1) != len(word2): return False
    
    # check if both words have the same unique letters
    c1 = Counter(word1)
    c2 = Counter(word2)
    if c1.keys() != c2.keys(): return False

    # check if there exists the same counts (non-unique)
    # this would allow op2 to work

    # if sorted(c1.values()) != sorted(c2.values()): return False
    # return True
  
    return sorted(c1.values()) == sorted(c2.values())