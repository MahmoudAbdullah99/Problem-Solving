class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):
            com = target-num
            if com in dict.keys():
                return [dict[com], index]
            else:
                dict[num] = index