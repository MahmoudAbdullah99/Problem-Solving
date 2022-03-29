class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        reversed_s = ""
        for i in range(len(s)-1,-1,-1):
            reversed_s += s[i]
        
        return reversed_s
    
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        reversed_words = [self.reverseString(list(word)) for word in words]
        return " ".join(reversed_words)