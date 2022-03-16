"""
Problem Description:
    - Given a string s, reverse the order of characters in each word within
    a sentence while still preserving whitespace and initial word order.

Notes:
    - 
    - 

TODO:
    - Review
"""

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
    
    def reverseWordsIndividually(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        reversed_words = [self.reverseString(list(word)) for word in words]
        return " ".join(reversed_words)
    
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev_word = ""
        rev_sentence = ""
        for i in range(len(s)):
            if s[i] == " ":
                rev_sentence += rev_word + " "
                rev_word = ""
            else:
                rev_word = s[i] + rev_word
        rev_sentence += rev_word
        return rev_sentence
