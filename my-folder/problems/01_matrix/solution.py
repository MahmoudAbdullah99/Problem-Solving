import math
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        zeros = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    zeros.append((i,j))
                else:
                    mat[i][j] = -1
        
        for r, c in zeros:
            if r > 0 and mat[r-1][c] == -1:
                mat[r-1][c] = mat[r][c] + 1
                zeros.append((r-1,c))
            
            if c > 0 and mat[r][c-1] == -1:
                mat[r][c-1] = mat[r][c] + 1
                zeros.append((r,c-1))
            
            if r+1 < len(mat) and mat[r+1][c] == -1:
                mat[r+1][c] = mat[r][c] + 1
                zeros.append((r+1,c))
            
            if c+1 < len(mat[0]) and mat[r][c+1] == -1:
                mat[r][c+1] = mat[r][c] + 1
                zeros.append((r,c+1))
            
        return mat
                