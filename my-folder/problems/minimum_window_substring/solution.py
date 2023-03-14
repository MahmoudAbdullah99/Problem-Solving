class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""

        t_chars, window = {}, {}
        
        for ch in t:
            t_chars[ch] = t_chars.get(ch, 0) + 1
        
        curr = 0
        sub_start, sub_len = -1, float("inf")
        l, r = 0, 0
        
        for r, ch in enumerate(s):
                        
            window[ch] = window.get(ch, 0) + 1
            
            if ch in t_chars and t_chars[ch] == window[ch]:
                curr += 1
            
            while curr == len(t_chars):
                if (r - l + 1) < sub_len:
                    sub_len = r - l + 1
                    sub_start = l
                
                window[s[l]] -= 1
                
                if s[l] in t_chars and t_chars[s[l]] > window[s[l]]:
                    curr -= 1
                
                l += 1
            
            r += 1
        
        if sub_len == float('inf'):
            return ""
                
        return s[sub_start:sub_start+sub_len]
        