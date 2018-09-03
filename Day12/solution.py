class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        m = [0, nums[1], nums[0], nums[0]]
        for n in nums[2:]:
            m = [max(m[:2]), m[0] + n, max(m[2:]), m[2] + n]
        return max(m[:-1])