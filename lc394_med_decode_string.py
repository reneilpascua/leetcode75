class Solution:
  def decodeString(self, s: str) -> str:
    multipliers = []
    strings = ['']
    
    i = 0
    while i < len(s):
      
      # capture multi-digit number
      full_num_str = ''
      while i < len(s) and s[i].isnumeric():
        full_num_str += s[i]
        i += 1
      if full_num_str: multipliers.append(int(full_num_str))
      
      c = s[i]
      if c.isalpha():
        strings[-1] += c
      elif c == '[':
        strings.append('')
      else: # c == ']'
        multiplier, string = multipliers.pop(), strings.pop()
        strings[-1] += multiplier*string
      i += 1
    return ''.join(strings)


if __name__ == '__main__':
  ex1 = "3[a]2[bc]" # aaabcbc
  ex2 = "3[a2[c]]" # accaccacc
  ex3 = "2[abc]3[cd]ef" # abcabccdcdcdef
  print(Solution().decodeString(ex3))