class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        choices=[9,9,8,7,6,5,4,3,2,1]
        p=1
        a=1
        for i in range(min(n,10)):
            p*=choices[i]
            a+=p
        return a
            
        