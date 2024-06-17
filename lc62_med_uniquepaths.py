class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    dp = [ [0 for _ in range(n)] for __ in range(m) ]
    # the top and left edges are 1s
    for i in range(n):
      dp[0][i] = 1
    for i in range(m):
      dp[i][0] = 1
    
    for i in range(1,m):
      for j in range(1,n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # print(dp)
    return dp[-1][-1]
  
if __name__ == '__main__':
  ex1 = (2,4)
  ex2 = (3,4)
  ex3 = (10,10)
  print(Solution().uniquePaths(*ex1))
  print(Solution().uniquePaths(*ex2))
  print(Solution().uniquePaths(*ex3))