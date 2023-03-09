class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        chars_indexes = set()
        l = 0
        
        for indx, char in enumerate(s):
            while char in chars_indexes:
                chars_indexes.remove(s[l])
                l += 1
            
            chars_indexes.add(char)
            longest_substring = max(indx - l + 1, longest_substring) 
            
        return longest_substring