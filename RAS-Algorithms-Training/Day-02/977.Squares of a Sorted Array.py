"""
Problem Description:
    Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
    non-decreasing order.

Notes:
    - The array is already sorted in a non-increasing order.

Steps:
    - Inverting order and sign of the negative numbers(putting them in the right order with respect to each other).
    - Iterating over them and the rest of the original list to put every element in their right order with respect to
    the rest of the original list.
    - Squaring the new list of the ordered elements.
"""


class Solution:
    def sortedSquares_no_sorting(self, nums):
        left = []
        right = []
        pointer = 0

        for index in range(len(nums)):
            if nums[index] < 0:
                left.insert(0, -nums[index])

            if nums[index] >= 0:
                right.extend(nums[index:])
                break

        for i in range(len(left)):
            while pointer < len(right):
                if left[i] <= right[pointer]:
                    right.insert(pointer, left[i])
                    pointer += 1
                    break
                pointer += 1
            if pointer == len(right):
                right.extend(left[i:])
                break

        return [num ** 2 for num in right]

    def sortedSquares(self, nums):
        return sorted([num ** 2 for num in nums])