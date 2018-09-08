class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(0,num+1):
            b=str(bin(i))
            l=len(b.split('1'))-1
            ans.append(l)
        return ans
            