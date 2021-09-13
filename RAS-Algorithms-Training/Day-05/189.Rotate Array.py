"""
Problem Description:
    Given an array, rotate the array to the right by k steps, where k is
    non-negative.

Notes:
    - If the number of steps 'k' is a multiple of the length of the list, then
    the list will remain as it is.
    - If the number of steps 'k' is smaller than the length of the list, then
    you just need to move the last k elements to the beginning of the list.
    - If the number of steps 'k' is bigger than the length of the list and is
    not a multiple of the length of the list, then you have no choice other
    than adding elements from the end of the list to the beginning one by one.

TODO:
    - Review.
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not k % len(nums):
            return
        elif k > len(nums):
            for i in range(k):
                nums.insert(0, nums[-1])
                nums.pop()
        else:
            nums[:] = nums[-k:] + nums[:-k]
