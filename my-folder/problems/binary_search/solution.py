class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            mid_element = nums[middle]
            
            if  target == mid_element:
                return middle
            elif target > mid_element:
                left = middle + 1
            else:
                right = middle - 1
        
        return -1