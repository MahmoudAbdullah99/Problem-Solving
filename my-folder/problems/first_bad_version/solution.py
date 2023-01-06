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
        l = 1
        r = n
        m = (l + r) // 2

        while l < r:
            if not isBadVersion(m):
                l = m + 1
            else:
                r = m
            m = (l + r) // 2
            
        
        return m