class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        
        for num in set(nums):
            counter[num] = 0
        
        for num in nums:
            counter[num] += 1

        return max(counter, key=counter.get)