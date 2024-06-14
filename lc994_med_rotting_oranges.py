from typing import List
from collections import deque

class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    H = len(grid)
    W = len(grid[0])
    oranges = 0
    roq = deque()
    # pass through the grid to find rotten oranges
    for i in range(H):
      for j in range(W):
        if not grid[i][j]: continue
        if grid[i][j] == 2:
          roq.append((i,j,0))
        oranges +=1
    # if len(roq) == 0: return -1 # there were no rottens found

    def get_tile(coord: tuple) -> int:
      nonlocal grid
      return grid[ coord[0] ][ coord[1] ]
    def inbounds(coord: tuple):
      nonlocal H, W
      return (0 <= coord[0] < H) and (0 <= coord[1] < W)
      
    visited = set()
    def enqueue_neighbors(i,j,mins):
      nonlocal roq, visited
      for new_coord in [(i,j-1),(i-1,j),(i,j+1),(i+1,j)]:
        if inbounds(new_coord) and new_coord not in visited and get_tile(new_coord) == 1:
          roq.append((*new_coord, mins+1))

    # bfs the rottens
    ans = 0
    while roq:
      print(roq)
      i,j,mins = roq.popleft()
      if (i,j) in visited: continue

      ans = mins
      visited.add((i,j))
      enqueue_neighbors(i,j,mins)

    return ans if len(visited) == oranges else -1

if __name__ == '__main__':
  ex1 = [
    [2,2],
    [1,1],
    [0,0],
    [2,0]
  ]
  print(Solution().orangesRotting(ex1))