from typing import List

class Solution:
  def __init__(self):
    self._letters = {
      '2': 'abc',
      '3': 'def',
      '4': 'ghi',
      '5': 'jkl',
      '6': 'mno',
      '7': 'pqrs',
      '8': 'tuv',
      '9': 'wxyz'
    }

  def letterCombinations(self, digits: str) -> List[str]:
    if not digits: return []

    # dfs
    ans = []
    def dfs(remaining_digits, pathsum):
      if not remaining_digits:
        ans.append(pathsum)
        return

      digit = remaining_digits[0]
      for letter in self._letters[digit]:
        dfs(remaining_digits[1:], pathsum+letter)

    dfs(digits, '')
    return ans
