class Solution:
  def reverseWords(self, s: str) -> str:
    splits = s.split(' ')
    return ' '.join(word.strip() for word in reversed(splits) if word)

if __name__ == '__main__':
  ex1 = 'the sky is blue'
  ex2 = '  hello world  '
  ex3 = 'a good   example'
  print(Solution().reverseWords(ex1))
  print(Solution().reverseWords(ex2))
  print(Solution().reverseWords(ex3))