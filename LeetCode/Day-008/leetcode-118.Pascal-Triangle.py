"""
Problem Description:
    - Given an integer numRows, return the first numRows of Pascal's triangle.
    - In Pascal's triangle, each number is the sum of the two numbersdirectly
    above it

Notes:
    - 
    - 

TODO:
    - Review
    - 
"""

class Solution(object):       
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rows = [[1]]
        for i in range(0, numRows-1):
            rows.append([1]+[rows[i][j]+rows[i][j+1] for j in range(len(rows[i])-1)] +[1])
        
        return rows