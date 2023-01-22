class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def calculate_area(i, j):
            if (not (0 <= i < len(grid))) or (not (0 <= j < len(grid[0]))) or grid[i][j] != 1:
                return 0
            
            grid[i][j] = -1
            return (1
                    + calculate_area(i-1, j)
                    + calculate_area(i+1, j)
                    + calculate_area(i, j-1)
                    + calculate_area(i, j+1))
        
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    temp_area = calculate_area(i,j)
                    max_area = max(max_area, temp_area)
        
        return(max_area)