"""
Problem Description:
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.

Notes:
    - A hash table is suitable for this approach by asserting the number of
    occurrences to the number, and returning the number with maximum
    occurrences.

Steps:
    - Iterating through the list, if the number is not in the hash table,
    then add it and assign 1 to it as the number of its occurrences. If the
    number is already in the hash table then increase the value assigned to
    it by 1.

TODO:
    - Review.
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        return max(counter, key=counter.get)

    def majorityElement_Fastest(self, nums: List[int]) -> int:
        counter = {}

        for num in set(nums):
            counter[num] = 0

        for num in nums:
            counter[num] += 1

        return max(counter, key=counter.get)
