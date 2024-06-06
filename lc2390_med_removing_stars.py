class Solution:
  def removeStars(self, s: str) -> str:
    stack = []
    for c in s:
      if c == '*':
        if stack: stack.pop()
      else:
        stack.append(c)

    return ''.join(stack)

if __name__ == '__main__':
  ex1 = 'leet**cod*e' # ans lecoe
  ex2 = 'erase*****' # ans empty string
  print(Solution().removeStars(ex1))
  print(Solution().removeStars(ex2))