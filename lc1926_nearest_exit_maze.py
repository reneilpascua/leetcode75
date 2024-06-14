from typing import List
from collections import deque
class Solution:

  # time limit exceeded
  def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
    H = len(maze)
    W = len(maze[0])

    visited = set()
    q = deque()
    q.append((*entrance, 0))

    def get_tile(coord: tuple):
      return maze[coord[0]][coord[1]]

    def inbounds(coord: tuple):
      nonlocal H, W
      return (0 <= coord[0] < H) and (0 <= coord[1] < W)

    def enqueue_neighbors(x, y, d):
      nonlocal visited, q
      for new_coord in [(x,y-1),(x-1,y),(x,y+1),(x+1,y)]:
        if inbounds(new_coord) and new_coord not in visited and get_tile(new_coord) == '.':
          q.append((*new_coord, d+1))


    # entrance cell cannot be an exit, so pop it and enqueue
    x, y, d = q.popleft()
    visited.add((x,y))
    enqueue_neighbors(x, y, d)
    while q:
      # print(q)
      x, y, d = q.popleft()
      if (x,y) in visited: continue
      visited.add((x,y))
      if (x in [0, H-1]) or (y in [0, W-1]): # is an exit
        return d
      enqueue_neighbors(x,y,d)
    return -1

if __name__ == '__main__':
  ex1 = (
    [
      ["+",".","+","+","+","+","+"],
      ["+",".","+",".",".",".","+"],
      ["+",".","+",".","+",".","+"],
      ["+",".",".",".","+",".","+"],
      ["+","+","+","+","+",".","+"]
    ],
    [3,2]
  ) # ans 4
  ex2 = (
    [
      ["+","+","+","+"],
      ["+",".",".","+"],
      ["+",".",".","+"],
      ["+","+","+","+"]
    ],
    [2,1]
  ) # -1
  print(Solution().nearestExit(*ex2))