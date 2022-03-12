class Solution(object):
    def naiveTwoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for indx_1 in range(len(nums)):
            for indx_2 in range(indx_1+1, len(nums)):
                if nums[indx_1] + nums[indx_2] == target:
                    return indx_1, indx_2