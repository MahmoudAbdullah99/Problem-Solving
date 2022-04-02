class Solution(object):
    def maxAreaOfIsland(self, grid):
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