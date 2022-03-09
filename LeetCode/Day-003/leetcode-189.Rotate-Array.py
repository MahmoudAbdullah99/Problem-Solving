"""
Problem Description:
    Given an array, rotate the array to the right by k steps, where k is
    non-negative.

Notes:
    - If the number of steps 'k' is a multiple of the length of the list, then
    the list will remain as it is.
    - If the number of steps 'k' is not a multiple of the length of the list,
    then you just need to move the last k elements to the beginning of the
    list.
    - Rotating by k steps where k is larger than the length of the list and is
    like rotating by (k % list_length).

TODO:
    - Review.
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) > 1 and k > 0:
            nums[:] = nums[-k:] + nums[:len(nums)-k]
