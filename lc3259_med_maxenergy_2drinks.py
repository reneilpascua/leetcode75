from typing import List

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dp = [[0, 0] for _ in range(n)] # space O(n)
        # dp[i][c] is the max energy at i'th hour if we choose energyDrink c
        # where c =0 if we drink A, and =1 if we drink B

        dp[0] = [energyDrinkA[0], energyDrinkB[0]]
        for i in range(1, n): # time O(n)
            dp[i][0] = energyDrinkA[i] + max( dp[i-1][0], dp[i-2][1] )
            dp[i][1] = energyDrinkB[i] + max( dp[i-2][0], dp[i-1][1] )
        
        # print(dp)
        return max(dp[-1][0], dp[-1][1])