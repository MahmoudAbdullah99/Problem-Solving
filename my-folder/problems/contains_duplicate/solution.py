class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        occurences = {}

        for ele in nums:
            if occurences.get(ele, 0) == 1:
                return True
            occurences[ele] = 1
        
        return False