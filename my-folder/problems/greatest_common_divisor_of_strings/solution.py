class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def validate(i):
            if len(str1) % i or len(str2) % i:
                return
            
            m = len(str1) // i
            n = len(str2) // i

            return str1[:i] * m == str1 and str1[:i] * n == str2

        for i in range(min(len(str1), len(str2)),0,-1):
            if validate(i):
                return str1[:i]
        
        return ""
