class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # To be mapable the two strtings must have the same number of charactes used to construct 
        if len(set(s)) != len(set(t)):
            return False
        
        mapping = dict()

        for i in range(len(s)):
            # Mapping characters from s to t
            if mapping.get(s[i], 0) == 0:
                mapping[s[i]] = t[i]
            # Passing for characters already saved in the mapping dictionary
            elif mapping.get(s[i], 0) != t[i]:
                return False
        
        return True
   