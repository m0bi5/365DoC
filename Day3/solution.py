<<<<<<< HEAD
class Solution:
    def rob(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        
        
                    
        dp=[0 for x in range(len(nums))]
        dp[0]=nums[0]
        dp[1]=max([nums[0],nums[1]])
        for i in range(2,len(nums)):
            dp[i]=max([dp[i-2]+nums[i],dp[i-1]])
=======
class Solution:
    def rob(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        
        
                    
        dp=[0 for x in range(len(nums))]
        dp[0]=nums[0]
        dp[1]=max([nums[0],nums[1]])
        for i in range(2,len(nums)):
            dp[i]=max([dp[i-2]+nums[i],dp[i-1]])
>>>>>>> d5fd9710d61c4eee60f3f76992db0ce470f40d30
        return dp[len(nums)-1]