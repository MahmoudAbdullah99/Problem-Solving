"""
Problem Description:
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
    return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.

Notes:
    - The array is already sorted in a non-increasing order.
    - The problem is similar to the binary search approach, but instead of returning -1 if you didn't find the target,
    you return the index where it should be

Steps:
    - Search using the binary search approach, and return the index of the target if exists.
    - If you did not find the target and it is larger than the last middle number in the list(the last indexed),
    return its index+1.
    - If you did not find the target and it is smaller than the last middle number in the list(the last indexed),
    return its index.

TODO:
    - Review.
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if target < nums[left]:
            return 0
        if target > nums[right]:
            return len(nums)

        while left <= right:
            middle = (left + right) // 2
            mid_element = nums[middle]

            if target == mid_element:
                return middle
            elif target > mid_element:
                left = middle + 1
            else:
                right = middle - 1

        return left
