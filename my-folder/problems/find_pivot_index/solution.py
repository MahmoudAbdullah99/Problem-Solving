class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # forming a running sum array
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        # side case when the pivot is the first element
        if nums[0] == nums[-1]:
            return 0
        # checking for a pivot
        for i in range(1, len(nums)):
            if nums[-1] - nums[i] == nums[i-1]:
                return i
        # did not find a pivot
        return -1