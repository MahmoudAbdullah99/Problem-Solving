class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not k % len(nums):
            return nums
        elif k < len(nums):
            nums[:] = nums[-k:] + nums[:-k]
        else:
            k = k % len(nums)
            for i in range(k):
                nums.insert(0, nums[-1])
                nums.pop()
