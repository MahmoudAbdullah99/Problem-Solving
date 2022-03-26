# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """        
        if n == 1: return 1
        
        left, right = 1, n
        
        while left <= right:
            version = (left+right)//2
            
            if isBadVersion(version):
                right = version-1
            else:
                left = version+1
        
        return left