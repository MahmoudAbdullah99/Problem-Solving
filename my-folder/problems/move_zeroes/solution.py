class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pointer, non_zero_pointer = 0, 0
        
        while zero_pointer < len(nums) and non_zero_pointer < len(nums):
            if nums[zero_pointer] != 0:
                non_zero_pointer += 1
                zero_pointer += 1
            elif nums[non_zero_pointer] == 0:
                non_zero_pointer += 1
            else:
                nums[non_zero_pointer], nums[zero_pointer] = nums[zero_pointer], nums[non_zero_pointer]
        
            