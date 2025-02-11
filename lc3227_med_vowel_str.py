from collections import Counter
class Solution_0:
    def doesAliceWin(self, s: str) -> bool:
        c = Counter(s)
        count = c['a']+c['e']+c['i']+c['o']+c['u']
        return count > 0

class Solution: # fastest
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a','e','i','o','u'}
        for c in s:
            if c in vowels: return True
        return False

# realized that as long as there is 1 vowel in the string, alice can win
# first sol goes through the str and counts all vowels
# second sol just stops once it sees any vowel