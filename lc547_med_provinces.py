from typing import List

class Solution:
  def findCircleNum(self, isConnected: List[List[int]]) -> int:
    # find number of disconnected graphs
    # can't just process isConnected sequentially bc of indirect connections
    
    provinces = 0
    seen = set()
    iterations = 0
    
    def explore(city_idx):
      nonlocal seen, isConnected, iterations
      # iterations += 1
      
      if city_idx in seen: return
      seen.add(city_idx)

      cxns = isConnected[city_idx]
      for i, cxn in enumerate(cxns):
        if cxn: explore(i)
      
    i = 0
    while i < len(isConnected):
      if i not in seen:
        provinces += 1
        explore(i)
      i += 1
    
    # print(iterations, 'iterations')
    return provinces