from typing import List

class Solution:
  def minReorder(self, n:int, connections: List[List[int]]) -> int:
    
    # different connection matrix
    cx_cities = [[] for _ in range(n)]
    for cxn in connections:
      cx_cities[ cxn[0] ].append( -cxn[1] )
      cx_cities[ cxn[1] ].append( cxn[0] )
    # NOTE: cx_cities[i] = [a, -b, c]
    # means city i has roads incoming from a & c, and is outgoing to b
    print(cx_cities)

    # dfs from city 0
    visited = set()
    reorders = 0
    def dfs(city):
      nonlocal cx_cities, reorders, visited
      print(city, visited)
      visited.add(city)
      for cxc in cx_cities[city]:
        abs_cxc = abs(cxc)
        if abs_cxc in visited: continue
        if cxc < 0:
          reorders += 1
        dfs(abs_cxc)
    dfs(0)
    return reorders



  # cant do this because memory limit exceeded... giant connection matrix
  def minReorder_matrix(self, n:int, connections: List[List[int]]) -> int:
    
    # create connection matrix
    edges = [ [0 for _ in range(n)] for __ in range(n) ]
    for cxn in connections:
      edges[ cxn[0] ][ cxn[1] ] = -1
      edges[ cxn[1] ][ cxn[0] ] = 1
    # NOTE: edges[i][j] = -1 means city i exits to city j

    # dfs from city 0
    visited = set()
    reorders = 0
    def dfs(city):
      nonlocal edges, reorders, visited
      visited.add(city)
      for i,edge in enumerate(edges[city]):
        if not edge: continue
        if i in visited: continue
        if edge == -1:
          reorders += 1
        dfs(i)
    
    # guaranteed fully connected graph, so WILL hit all cities
    dfs(0)
    return reorders

if __name__ == '__main__':
  ex1 = (6, [[0,1],[1,3],[2,3],[4,0],[4,5]])
  print(Solution().minReorder(*ex1))