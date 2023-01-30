class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {k: v for v,k in enumerate(nums)}

        for i in range(len(nums)):
            if hash_table.get(target-nums[i]) and i != hash_table[target-nums[i]]:
                return i, hash_table[target-nums[i]]
