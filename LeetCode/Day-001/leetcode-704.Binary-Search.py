class Solution:
    def iterative_search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            mid_element = nums[middle]

            if target == mid_element:
                return middle
            elif target > mid_element:
                left = middle + 1
            else:
                right = middle - 1

        return -1

    def recursive_search(self, nums, target, left=0, right=None) -> int:
        if right is None: right = len(nums) - 1
        if left > right:
            return -1
        else:
            middle_index = (left + right) // 2
            middle_element = nums[middle_index]
            if target == middle_element:
                return middle_index
            elif target > middle_element:
                return self.recursive_search(nums, target, middle_index + 1, right)
            else:
                return self.recursive_search(nums, target, left, middle_index - 1)