class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2)<len(s1):
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for i in range(len(s1)):
            s1_count[ord(s1[i])-97] += 1
            s2_count[ord(s2[i])-97] += 1
                
        for i in range(len(s1), len(s2)+1):
            if s1_count == s2_count:
                return True
            
            if i < (len(s2)):
                s2_count[ord(s2[i])-97] += 1
            
            s2_count[ord(s2[i-len(s1)])-97] -= 1
            
        return False