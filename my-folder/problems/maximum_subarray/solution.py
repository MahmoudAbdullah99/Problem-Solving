class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -(10**4)-1
        temp_max = 0

        for num in nums:
            temp_max += num
            if max_sum < temp_max:
                max_sum = temp_max
            
            if temp_max < 0:
                temp_max = 0
        
        return max_sum