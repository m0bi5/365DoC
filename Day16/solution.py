class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0 for _ in range(0,amount+1)]
        for i in range(1,amount+1):
            mi=float('inf')
            for coin in coins:
                if i-coin>=0:
                    mi = min(dp[i-coin]+1,mi) 
            dp[i]=mi 
        if dp[amount] == float('inf'):
            return -1 
        else:
            return dp[amount]