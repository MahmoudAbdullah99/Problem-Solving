class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = -1, -1
        for index, num in enumerate(nums):
            if num == target:
                l = index
                break
        for index, num in enumerate(nums):
            if num == target:
                r = index
        return [l, r]