from collections import deque
from time import sleep
class Solution:
  def predictPartyVictory(self, senate: str) -> str:
    N = len(senate)
    banned = set()
    rq = deque() # radiant queue
    dq = deque() # dire queue
    iteration = 0

    def reload():
      """
      enqueues unbanned senate members in rq and dq, gives them a number
      indicating order (uses mod N)
      """
      nonlocal N, banned, rq, dq, senate, iteration
      for i, s in enumerate(senate):
        if i not in banned:
          modded_order = N*iteration + i
          rq.append(modded_order) if s == 'R' else dq.append(modded_order)
      iteration += 1
      # print('reloaded','r',rq,'d',dq)
      # sleep(1)

    reload()
    while rq and dq:
      if rq[0] < dq[0]: # radiant goes
        rq.popleft()
        banned.add(dq.popleft()%N)
      else: # dire goes
        dq.popleft()
        banned.add(rq.popleft()%N)
      
      # reload if empty
      if not (rq and dq):
        reload()
    else:
      return 'Radiant' if rq else 'Dire'

if __name__ == '__main__':
  ex1 = "RD"
  ex2 = "RDD"
  print(Solution().predictPartyVictory(ex1))
  print(Solution().predictPartyVictory(ex2))