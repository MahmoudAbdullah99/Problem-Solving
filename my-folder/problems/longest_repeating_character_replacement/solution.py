class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_count = 0
        chars_count = [0] * 26
        
        while r < len(s):
            curr_char_place = ord(s[r]) - ord('A')
            chars_count[curr_char_place] += 1
            max_count = max(max_count, chars_count[curr_char_place])
            
            while ((r - l + 1) - max_count) > k:
                chars_count[ord(s[l]) - ord('A')] -= 1                    
                l += 1
            
            r += 1
        
        return r - l