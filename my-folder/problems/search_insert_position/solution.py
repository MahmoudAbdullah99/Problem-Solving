class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if target < nums[left]:
            return 0
        if target > nums[right]:
            return len(nums)

        while left <= right:
            middle = (left + right) // 2
            mid_element = nums[middle]

            if target == mid_element:
                return middle
            elif target > mid_element:
                left = middle + 1
            else:
                right = middle - 1

        return left
        