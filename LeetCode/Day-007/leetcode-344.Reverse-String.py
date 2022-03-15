"""
Problem Description:
    - Write a function that reverses a string. The input string is given as an
    array of characters s.
    - You must do this by modifying the input array in-place with O(1) extra
    memory.

Notes:
    - 
    - 

TODO:
    - Riview
"""

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
