class Solution:
    def reverseWords(self, s: str) -> str:
        rev_word = ""
        for i in range(len(s)-1,-2,-1):
            if i == -1 or s[i] == ' ':
                s = s[:i+1] + rev_word + s[i+1+len(rev_word):]
                rev_word = ""
                continue
            rev_word += s[i]
        return s