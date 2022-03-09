"""
Problem Description:
    Given an integer array nums sorted in non-decreasing order, return an
    array of the squares of each number sorted in non-decreasing order.

Notes:
    - The array is already sorted in a non-increasing order.

Steps:
    - Inverting order and sign of the negative numbers(putting them in the
    right order with respect to each other).
    - Iterating over them and the rest of the original list to put every
    element in their right order with respect to the rest of the original list.
    - Squaring the new list of the ordered elements.

TODO:
    - Review.
"""

class Solution(object):
    def naiveSortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [i**2 for i in nums]
        nums.sort()
        return nums
    
    def optimizedSortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares = []
        positives = []
        negatives = []
        barrier = 0

        for indx, ele in enumerate(nums):
            if ele < 0:
                barrier+=1
            else:
                positives.append(ele**2)

        for indx in range(barrier-1,-1,-1):
            negatives.append(nums[indx]**2)
        
        pos_indx, neg_indx = 0, 0

        while pos_indx < len(positives) and neg_indx < len(negatives):
            if positives[pos_indx] == negatives[neg_indx]:
                squares.extend([positives[pos_indx], negatives[neg_indx]])
                pos_indx += 1
                neg_indx += 1
            elif positives[pos_indx] < negatives[neg_indx]:
                squares.append(positives[pos_indx])
                pos_indx += 1
            else:
                squares.append(negatives[neg_indx])
                neg_indx += 1

        while pos_indx < len(positives):
            squares.append(positives[pos_indx])
            pos_indx += 1
        
        while neg_indx < len(negatives):
            squares.append(negatives[neg_indx])
            neg_indx += 1

        return squares
