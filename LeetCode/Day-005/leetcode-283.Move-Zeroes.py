class Solution(object):
    def moveZeroesExternalArray(self, nums):
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
    
    def moveZeroesTwoPointers(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pointer1 = 0
        pointer2 = 1

        while pointer1 < len(nums) and pointer2 < len(nums):
            if nums[pointer1] != 0:
                pointer1 += 1
                pointer2 += 1
            elif nums[pointer1] == 0 and nums[pointer2] != 0:
                nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
                pointer1 += 1
                pointer2 += 1
            elif nums[pointer1] == 0 and nums[pointer2] == 0:
                pointer2 += 1
        
        print(nums)


sol = Solution()
nums = [1,2,3,0]
sol.moveZeroesTwoPointers(nums)