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
        dict_nums = {}
        for num in nums:
                if dict_nums.get(num):
                    dict_nums[num] += 1
                else:
                    dict_nums[num] = 1
        
        return dict_nums

    def intersectHashTable(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersections = []
        if len(nums1) > len(nums2):
            dict_nums = self.makeDictionary(nums2)
            nums = nums1
        else:
            dict_nums = self.makeDictionary(nums1)
            nums = nums2
        
        for num in nums:
            if dict_nums.get(num):
                intersections.append(num)
                dict_nums[num] -= 1
        
        return intersections
