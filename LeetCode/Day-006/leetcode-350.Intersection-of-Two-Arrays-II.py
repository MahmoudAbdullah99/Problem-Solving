"""
Problem Description:
    - Given two integer arrays nums1 and nums2, return an array of their
    intersection. Each element in the result must appear as many times as it
    shows in both arrays and you may return the result in any order.

Notes:
    - 

TODO:
    - Add notes
    - Review.
"""

class Solution(object):
    def makeDictionary(self, nums):
        """
        :type nums: List[int]
        :rtype: Dict
        """
        dict_nums = {}
        for num in nums:
            dict_nums[num] = dict_nums.get(num,0) + 1
        return dict_nums

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersections = []
        dict_nums = self.makeDictionary(nums2)
        
        for num in nums1:
            if dict_nums.get(num):
                intersections.append(num)
                dict_nums[num] -= 1
        
        return intersections
