class Solution(object):
    def naiveContainsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for indx, ele in enumerate(nums):
            for i in range(indx+1, len(nums)):
                if ele == nums[i]:
                    return True
        
        return False

    def optimizedContainsDuplicate(self, nums):
        occurences = {}

        for ele in nums:
            if occurences.get(ele, 0) == 1:
                return True
            occurences[ele] = 1
        
        return False
