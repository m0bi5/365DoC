class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        
        profit=0
        minprice=999999999999
        for i in prices:
            if i<minprice:
                minprice=i
            elif i-minprice>profit:
                profit=i-minprice
        return profit