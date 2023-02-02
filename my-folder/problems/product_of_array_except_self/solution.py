class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_products = [1] * len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            total_products[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            total_products[i] *= postfix
            postfix *= nums[i]

        return total_products