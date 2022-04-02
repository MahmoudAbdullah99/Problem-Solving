"""
Problem Description:
    -
    - 

Notes:
    - 
    - 

TODO:
    - 
    - 
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(r, c):
            if (not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or
            grid[r][c] in [0, -1]):
                return 0
            
            if grid[r][c] == 1:
                grid[r][c] = -1
            
            left_area  = dfs(r, c-1)
            right_area = dfs(r, c+1)
            above_area = dfs(r-1, c)
            below_area = dfs(r+1, c)

            return 1 + left_area + right_area + above_area + below_area
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr_area = dfs(i, j)
                    max_area = max(max_area, curr_area)
        
        return max_area