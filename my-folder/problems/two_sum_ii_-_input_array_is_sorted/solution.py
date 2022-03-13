class Solution(object):    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_pointer, right_pointer = 0, len(nums)-1

        while left_pointer < right_pointer:
            if nums[left_pointer] + nums[right_pointer] == target:
                return [left_pointer+1, right_pointer+1]
            elif nums[left_pointer] + nums[right_pointer] > target:
                right_pointer -= 1
            else:
                left_pointer += 1