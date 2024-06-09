from collections import deque
class RecentCounter:
  """
  counts number of recent requests within a certain time frame
  """
  def __init__(self):
    """
    initializes the counter with zero recent requests
    """
    self.reqs = deque()

  def ping(self, t: int) -> int:
    """
    adds a new request at time t.
    returns number of requests that have happened in the past 3000
    (inclusive time range of [t-3000,t])
    """
    self.reqs.appendleft(t)
    while self.reqs[-1] < t-3000:
      self.reqs.pop()
    return len(self.reqs)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)