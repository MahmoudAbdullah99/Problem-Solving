class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            mid_element = nums[middle]
            
            if  target < mid_element:
                right = middle - 1
            elif target > mid_element:
                left = middle + 1
            else:
                return middle
        
        return -1