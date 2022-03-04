class Solution(object):
    def search(self, nums, target, left=0, right=None):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if right == None:
            right = len(nums) - 1
        
        if left > right:
            return - 1
        
        mid_index = (left + right) // 2
        mid = nums[mid_index]
                
        if mid == target:
            return mid_index
        elif mid > target:
            return(self.search(nums, target, left, mid_index-1))
        else:
            return(self.search(nums, target, mid_index+1, right))