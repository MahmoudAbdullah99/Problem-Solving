class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = -1, -1
        i = 0
        j = len(nums) - 1
        
        while i < len(nums):
            if nums[i] == target:
                l = i
                break
            i += 1
        
        while j >= i:
            if nums[j] == target:
                r = j
                break
            j -= 1
            
        return [l, r]