class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_index = {}

        for num in nums:
            if nums_index.get(num) != None:
                return True
            
            nums_index[num] = index
        
        return False