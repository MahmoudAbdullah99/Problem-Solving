"""
TODO: complete maxCrossingSum funcrion
"""

class Solution(object):
    def linearMaxSubArray(self, nums):
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

    def maxCrossingSum(arr, left, mid, right):
        
        pass

    def dc_MaxSubArray(self, nums, left, right):
        
        if left == right:
            return nums[left]

        mid = (left+right)//2

        left_sum = self.dc_MaxSubArray(nums, left, mid)
        right_sum = self.dc_MaxSubArray(nums, mid+1, right)
        cross_sum = self.maxCrossingSum(nums, left, mid, right)
        
        return max(left_sum, right_sum, cross_sum)

        pass


sol = Solution()
nums = [5,4,-1,7,8]
print(sol.linearMaxSubArray(nums))
nums = [5]
print(sol.linearMaxSubArray(nums))
nums = [5,-5]
print(sol.linearMaxSubArray(nums))
nums = [-5,5]
print(sol.linearMaxSubArray(nums))
nums = [-5,-5]
print(sol.linearMaxSubArray(nums))
nums = [5,1,-1,1,-1,1,-2,5]
print(sol.linearMaxSubArray(nums))