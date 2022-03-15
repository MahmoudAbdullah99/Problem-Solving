class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        for i in range(len_s//2):
            opposite = len_s-i-1
            temp = s[i]
            s[i] = s[opposite]
            s[opposite] = temp
