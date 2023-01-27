class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        minutes = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten.append((r, c, minutes))
        
        for r, c, minutes in rotten:
            for new_r, new_c in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                if new_r >= 0 and new_r < len(grid) and new_c >= 0 and new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 2
                    rotten.append((new_r, new_c, minutes+1))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        
        return minutes       