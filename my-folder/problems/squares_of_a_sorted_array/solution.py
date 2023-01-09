class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(nums)-1
        c = len(nums)-1
        sq_nums = [0] * len(nums)

        while c >= 0:
            left_sq = nums[i] ** 2
            right_sq = nums[j] ** 2

            if left_sq >= right_sq:
                sq_nums[c] = left_sq
                i += 1
            else:
                sq_nums[c] = right_sq
                j -= 1
            c -= 1

        return sq_nums