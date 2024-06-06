from typing import List
class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    state = []
    for asteroid in asteroids:
      asteroid_broken = False
      while state and state[-1] > 0 and asteroid < 0: # converging
        # a collision occurs
        sz_asteroid, sz_previous = abs(asteroid), abs(state[-1])
        if sz_asteroid > sz_previous:
          state.pop()
        else:
          if sz_asteroid == sz_previous: state.pop()
          asteroid_broken = True
          break

      if not asteroid_broken: state.append(asteroid)
    return state

if __name__ == '__main__':
  ex1 = [5,10,-5]
  ex2 = [8,-8]
  ex3 = [10,2,-5]
  print(Solution().asteroidCollision(ex1))
  print(Solution().asteroidCollision(ex2))
  print(Solution().asteroidCollision(ex3))