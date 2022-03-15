class Solution(object):
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
