"""
Problem Description:
    - Given a 1-indexed array of integers numbers that is already sorted in
    non-decreasing order, find two numbers such that they add up to a specific
    target number. Let these two numbers be numbers[index1] and numbers[index2]
    where 1 <= index1 < index2 <= numbers.length.
    - Return the indices of the two numbers, index1 and index2, added by one
    as an integer array [index1, index2] of length 2.
    - The tests are generated such that there is exactly one solution. You may
    not use the same element twice.
    - Your solution must use only constant extra space.

Notes:
    - 

TODO:
    - Add notes
    - Review.
"""

class Solution(object):
    def binarySearch(self, nums, target, left=None, right=None):
        if left == None:
            left = 0
        
        if right == None:
            right = len(nums)-1
        
        print(nums[left:right+1])
        print(target)
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        
        return
    
    def twoSumBinarySearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for indx1 in range(len(nums)):
            indx2 = self.binarySearch(nums, target-nums[indx1], left=indx1+1)
            print(indx1, indx2)
            if indx2 != None and indx1 != indx2:
                return [indx1+1, indx2+1]
    
    def twoSumTwoPointers(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_pointer, right_pointer = 0, len(nums)-1

        while left_pointer < right_pointer:
            if nums[left_pointer] + nums[right_pointer] == target:
                return [left_pointer+1, right_pointer+1]
            elif nums[left_pointer] + nums[right_pointer] > target:
                right_pointer -= 1
            else:
                left_pointer += 1
