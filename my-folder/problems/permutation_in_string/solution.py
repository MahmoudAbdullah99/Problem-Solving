class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counter = {k:0 for k in s1+s2}
        s2_counter = {k:0 for k in s1+s2}

        for i in range(len(s1)):
            s1_counter[s1[i]] += 1
            s2_counter[s2[i]] += 1
        
        for i in range(len(s1), len(s2)+1):
            if s1_counter == s2_counter:
                return True
            
            if i < len(s2):
                s2_counter[s2[i]] += 1
            
            s2_counter[s2[i-len(s1)]] -= 1
        
        return False