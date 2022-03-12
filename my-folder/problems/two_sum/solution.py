class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {k: v for v, k in enumerate(nums)}
        for indx_1 in range(len(nums)):
            indx_2 = nums_dict.get(target - nums[indx_1])
            if indx_2 != None and indx_1 != indx_2:
                return indx_1, indx_2