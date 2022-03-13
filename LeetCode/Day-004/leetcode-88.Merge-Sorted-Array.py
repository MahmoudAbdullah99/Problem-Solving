"""
Problem Description:
    - You are given two integer arrays nums1 and nums2, sorted in non-decreasing
    order, and two integers m and n, representing the number of elements in
    nums1 and nums2 respectively.
    - Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    - The final sorted array should not be returned by the function, but
    instead be stored inside the array nums1. To accommodate this, nums1 has
    a length of m + n, where the first m elements denote the elements that
    should be merged, and the last n elements are set to 0 and should be
    ignored. nums2 has a length of n.

Notes:
    - 

TODO:
    - Add notes
    - Review.
"""


class Solution(object):
    def mergeInPlace(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        indx_1, indx_2, pointer = 0, 0, m

        if m == 0:
            nums1[:] = nums2
            return
        elif n == 0:
            return
        
        while indx_1 < m and indx_2 < n:
            if nums1[indx_1] <= nums2[indx_2]:
                if pointer < m+n:
                    nums1[pointer] = nums1[indx_1]
                else:
                    nums1.append(nums1[indx_1])
                indx_1 += 1
            else:
                if pointer < m+n:
                    nums1[pointer] = nums2[indx_2]
                else:
                    nums1.append(nums2[indx_2])
                indx_2 += 1
            pointer += 1

        while pointer < len(nums1):
            nums1.pop()
                
        if indx_1 < m:
            nums1.extend(nums1[indx_1:m])
        
        if indx_2 < n:
            diff = n-indx_2
            nums1.extend(nums2[indx_2:n])
        
        nums1[:] = nums1[m:]
