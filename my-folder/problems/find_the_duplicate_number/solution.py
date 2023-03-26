class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n1, n2 = 0, 0
        while True:
            n1 = nums[n1]
            n2 = nums[nums[n2]]
            
            if n1 == n2:
                break
        
        n2 = 0
        
        while True:
            n1 = nums[n1]
            n2 = nums[n2]
            
            if n1 == n2:
                return n1