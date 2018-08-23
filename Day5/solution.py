class NumArray:
    n=[]

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n=nums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.n[i:j+1])
        