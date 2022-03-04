# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1: return 1
        
        left, right = 1, n
        
        while left <= right:
            version = (left+right)//2
            
            if isBadVersion(version) is True:
                right = version-1
            else:
                left = version+1
        
        return left