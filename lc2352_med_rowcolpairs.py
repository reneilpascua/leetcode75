from collections import Counter
from typing import List
class Solution:
  def equalPairs(self, grid: List[List[int]]) -> int:
    """
    inspiration from solutions:
    hash the rows of the grid, but turn row into tuple (array is not hashable).
    --> can count how many times the same row appears
    in same way, hash COLS of grid, then compare

    to hash the cols, transpose it using zip(*grid) which gives tuples already
    """
    
    # tuple(my_array) will turn my_array into a tuple
    # to tuplefy each row of the grid, use map(tuple, grid)
    row_counts = Counter(map(tuple,grid))

    col_counts = Counter(zip(*grid))

    # say row X occurs N times, and row X matches col Y which occurs M times
    # the total pairings is N*M
    return sum([row_counts[row]*col_counts[row] for row in row_counts])
  
  def equalPairs_0(self, grid: List[List[int]]) -> int:
    n = len(grid)

    # look at grid[i][j]
    # colJ is still valid for rowI IF colJ[j] == grid[i][j]
    # next is grid[i][j+1]
    # colJ is still valid for rowI IF colJ[j+1] == grid[i][j+1]

    def check_cols(cols_to_check: set, k: int, val: int):
      """
      Iterates through the columns and compares their k'th element to val
      """
      nonlocal grid
      for col_idx in list(cols_to_check):
        if grid[k][col_idx] != val:
          cols_to_check.remove(col_idx)

    pairs = 0
    for row in grid:
      valid_cols = { j for j in range(n) }
      for j in range(n):
        check_cols(valid_cols, j, row[j])
      pairs += len(valid_cols)

    return pairs

if __name__ == '__main__':
  ex1 = [[3,2,1],[1,7,6],[2,7,7]] # ans 1
  ex2 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]] # ans 3
  print(Solution().equalPairs(ex1))
  print(Solution().equalPairs(ex2))