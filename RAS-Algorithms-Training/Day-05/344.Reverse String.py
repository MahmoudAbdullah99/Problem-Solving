"""
Problem Description:
    Write a function that reverses a string. The input string is given as an
    array of characters s.

Notes:
    - When reading, list is a reference to the original list, and list[:]
    shallow-copies the list.
    - When assigning, list (re)binds the name and list[:] slice-assigns,
    replacing what was previously in the list.

TODO:
    - Review.
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = [s[i] for i in range(len(s)-1,-1,-1)]
