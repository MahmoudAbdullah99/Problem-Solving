class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ls = [sum(nums[:i+1]) for i in range(len(nums))]
        return ls