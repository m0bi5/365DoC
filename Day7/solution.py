class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ret = max_num = min_num = nums[0]
        for num in nums[1:]:
            min_num, _, max_num = sorted([num, num * max_num, num * min_num])
            ret = max(max_num, ret)
        return ret