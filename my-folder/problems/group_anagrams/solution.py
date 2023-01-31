from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = defaultdict(list)
        for word in strs:
            count_chars = [0] * 26
            
            for char in word:
                count_chars[ord(char)-97] += 1
            
            hashes[str(count_chars)].append(word)
                
        return hashes.values()