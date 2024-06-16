from typing import List

class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    self.dp = {0: cost[0], 1: cost[1]}
    i = 2
    while i < len(cost):
      self.dp[i] = cost[i] + min(self.dp[i-1], self.dp[i-2])
      i += 1
    return min(self.dp[i-1], self.dp[i-2])