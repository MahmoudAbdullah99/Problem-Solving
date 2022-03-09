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
