class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n+1)
        for i in xrange(1, int(n**0.5)+1):
            dp[i**2] = 1

        for i in xrange(1, n+1):
            for k in xrange(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-k**2]+1)

        return dp[n]