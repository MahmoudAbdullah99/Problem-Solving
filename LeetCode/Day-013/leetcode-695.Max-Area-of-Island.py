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
    def maxAreaOfIslandDFS(self, grid):
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
    
    def maxAreaOfIslandQueue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def island_size(r, c):
            area = 0
            cells = [(r, c)]
            
            while len(cells):
                r, c = cells.pop()
                
                if grid[r][c] == -1:
                    continue
                
                # -1 represents checked cells
                grid[r][c] = -1
                area += 1
                
                if r < len(grid)-1 and grid[r+1][c] == 1:
                    cells.append((r+1, c))
                if c < len(grid[0])-1 and grid[r][c+1] == 1:
                    cells.append((r, c+1))
                if r > 0 and grid[r-1][c] == 1:
                    cells.append((r-1, c))
                if c > 0 and grid[r][c-1] == 1:
                    cells.append((r, c-1))
            
            return area
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr_area = island_size(i, j)
                    max_area = max(max_area, curr_area)
        
        return max_area