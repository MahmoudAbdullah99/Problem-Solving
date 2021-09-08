"""
Problem Description:
    Let's call an array arr a mountain if the following properties hold:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... arr[i-1] < arr[i]
        arr[i] > arr[i+1] > ... > arr[arr.length - 1]

    Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] <
     ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Notes:
    - You only need to find the index of the greatest number (the top of the mountain).
    - The problem is similar to the binary search approach, but instead of comparing the middle number to the target,
    you need to compare the middle number to the two numbers next to it.
"""

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            middle = (left + right) // 2
            if arr[middle] > arr[middle-1]:
                if arr[middle] > arr[middle+1]:
                    return middle
                else:
                    left = middle
            else:
                right = middle