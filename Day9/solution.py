class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1=nums[0]
        m2=nums[0]
        for i in range(1,len(nums)):
            m1=max(nums[i],nums[i]+m1)
            m2=max(m1,m2)
        return m2