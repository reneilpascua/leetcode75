from typing import List

class Solution:
  def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    visited = {0}
    keys = rooms[0][:]

    while keys:
      key = keys.pop()
      if key not in visited:
        visited.add(key)
        keys += rooms[key]

    return len(visited) == len(rooms)