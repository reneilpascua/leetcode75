class Solution:
  def maxVowels(self, s: str, k: int) -> int:
    vset = set(['a','e','i','o','u'])
    def isvowel(c) -> bool:
      nonlocal vset
      return c in vset

    vcount = 0
    vmax = 0
    i = 0
    while i < len(s):
      if i < k: # hasnt reached max window size;
        vcount += 1 if isvowel(s[i]) else 0
      else:
        if isvowel(s[i]):
          vcount += 1
        if isvowel(s[i-k]):
          vcount -= 1
      vmax = max(vmax, vcount)
      i+=1
    
    return vmax