from collections import defaultdict, deque
from typing import List
class Solution:

  # i thought this had much better memoization, but it didn't make a big diff
  # in time
  def calcEquation_dfs(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    
    # d[op1][op2] is the answer to op1/op2
    d = defaultdict(dict)
    for eqn, val in zip(equations, values):
      d[ eqn[0] ][ eqn[1] ] = val
      d[ eqn[1] ][ eqn[0] ] = 1/val

    for k in d:
      d[k][k] = 1
    
    def dfs(op1, visited: set) -> dict:
      """
      explores every op2 connected to op1 and returns a dict of quotients.
      pathsum is the trip's value as it arrives into op1
      """
      nonlocal d
      visited.add(op1)

      # make a copy of d[op1] AT THIS TIME (it may be added to)
      neighbors = {k:v for k,v in d[op1].items()}

      for op2 in neighbors:
        if op2 in visited: continue
        qd = dfs(op2, visited)
        for op3 in qd:
          if op3 not in d[op1]:
            d[op1][op3] = d[op1][op2]*d[op2][op3]

      return d[op1]
    
    ans = []
    for op1, op2 in queries:
      if not (op1 in d and op2 in d): # there's an undefined var
        ans.append(-1)
        continue
      
      if op2 not in d[op1]:
        dfs(op1, set()) # full traversal (does not stop at op2)
      ans.append(d[op1][op2] if op2 in d[op1] else -1)
      
    return ans

  # NEEDS BETTER MEMOIZATION. the big while-loop only saves answers for the first city.
  def calcEquation_0(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    # NOTE: use a graph here bc this problem was under the graph section,
    # but i would not have thought to use a graph...
    # NOTE: CYCLES ARE ALLOWED

    # create a dict of dicts for "travel cost"
    # d['a'] is a dict of costs to travel from 'a' to its connected cities
    # d['a']['b'] is the cost to travel from 'a' to 'b'
    # note that d['b']['a'] is the reciprocal of d['a']['b']
    d = defaultdict(dict)
    for eqn, val in zip(equations, values):
      d[ eqn[0] ][ eqn[1] ] = val
      d[ eqn[1] ][ eqn[0] ] = 1/val
    
    # a city travelling to itself is 1
    for k in d:
      d[k][k] = 1
    
    ans = []
    for op1, op2 in queries:
      if not (op1 in d and op2 in d): # there's an undefined var
        ans.append(-1)
        continue
      
      if op2 not in d[op1]: # gotta traverse for the answer
        visited = {op1}
        s = [ (city, cost) for city, cost in d[op1].items() if city not in visited ]
        while s:
          curcity, curcost = s.pop()
          if curcity in visited:
            continue
          visited.add(curcity)
          if curcity not in d[op1]:
            d[op1][curcity] = curcost
          if curcity == op2: break
          s += [ (city, curcost*cost) for city, cost in d[curcity].items() if city not in visited ]

      ans.append(d[op1][op2] if op2 in d[op1] else -1)
    print(d)
    return ans

if __name__ == '__main__':
  ex1 = ([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
  print(Solution().calcEquation(*ex1))