"""
Problem Description:
    - Given an array of integers nums and an integer target, return indices of
    the two numbers such that they add up to target.
    - You may assume that each input would have exactly one solution, and you
    may not use the same element twice.
    - You can return the answer in any order.

Notes:
    - 

TODO:
    - Add notes.
    - Review.
"""

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
    
    def optimizedTwoSum(self, nums, target):
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
