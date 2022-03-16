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