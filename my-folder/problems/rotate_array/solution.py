class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = len(nums) - (k % len(nums))
        for i in range(pointer):
            nums.append(nums[i])
        nums[:] = nums[pointer:]