# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
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

