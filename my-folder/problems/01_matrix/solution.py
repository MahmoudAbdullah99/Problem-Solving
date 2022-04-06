class Solution:
    def updateMatrix(self, mat):
        queue = []
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c]= -1
                    
        
        for r, c in queue:
            for new_r, new_c in [(r-1, c),(r, c-1),(r+1, c),(r, c+1)]:
                if new_r >= 0 and new_r < len(mat) and new_c >= 0 and new_c < len(mat[0]) and mat[new_r][new_c] == -1:
                    mat[new_r][new_c] = mat[r][c]+1
                    queue.append((new_r,new_c))
                    
        return mat