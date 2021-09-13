"""
Problem Description:
    Given an array of integers nums sorted in ascending order, find the starting
    and ending position of a given target value.
    If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Notes:
    - The array is already sorted in a ascending order.
    - You need only to find the start and the end indexes of the occurrences
    of the target, so no need to get through the whole list.

Steps:
    - Iterate from the start of the array in an ascending order indexing, and
    stop when you find the first occurrence of the target(the start).
    - Iterate from the end of the array in a descending order indexing, and
    stop when you find the first occurrence of the target(the end).
    - If you did not find any occurrence of the target return [-1, -1],
    else return the first and last occurrences of the target [start, end].

TODO:
    - Review.
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        i = 0
        j = len(nums) - 1

        while i < len(nums):
            if nums[i] == target:
                start = i
                break
            i += 1

        while j >= i:
            if nums[j] == target:
                end = j
                break
            j -= 1

        return [start, end]