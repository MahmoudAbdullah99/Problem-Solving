class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros_counter = 0
        temp_nums = []
        for num in nums:
            if num != 0:
                temp_nums.append(num)
            else:
                zeros_counter += 1
        
        nums[:] = temp_nums + zeros_counter*[0]
