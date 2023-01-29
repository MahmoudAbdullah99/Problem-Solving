class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table = {}

        for char in s:
            if hash_table.get(char) == None:
                hash_table[char] = 1
                continue
            
            hash_table[char] += 1
        
        for char in t:
            if hash_table.get(char) == None:
                return False

            hash_table[char] -= 1

        for k,v in hash_table.items():
            if v != 0:
                return False
        
        return True