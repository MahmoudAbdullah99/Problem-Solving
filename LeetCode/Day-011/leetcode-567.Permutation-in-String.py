"""
Problem Description:
    - Given two strings s1 and s2, return true if s2 contains a
    permutation of s1, or false otherwise.
    - In other words, return true if one of s1's permutations is the
    substring of s2. 

Notes:
    - 
    - 

TODO:
    - Add notes
    - Review
"""

from collections import Counter


class Solution():
    def checkInclusionCounter(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        
        s1_chars = Counter(s1)

        for i in range(len(s2)-len(s1)+1):
            temp_counter = Counter(s2[i:i+len(s1)])
            if s1_chars == temp_counter:
                return True
        
        return False
