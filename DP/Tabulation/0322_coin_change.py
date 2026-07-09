"""
    Level: Medium
    Problem:
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.

    Example 1:

    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

    Example 2:

    Input: coins = [2], amount = 3
    Output: -1

    Constraints:

    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104.

"""

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        r,c = len(coins),amount+1
        dp = [[float('inf')]*c for _ in range(r)]
        for i in range(r):
            dp[i][0] = 0
        for i in range(r):
            for j in range(1,c):
                if j < coins[i]: 
                    dp[i][j] = dp[i-1][j]
                else: dp[i][j] = min(dp[i-1][j] , 1 + dp[i][j-coins[i]])
            print(*dp[i])
        
        if dp[-1][-1] == float('inf'): return -1
        return dp[r-1][c-1]
        
