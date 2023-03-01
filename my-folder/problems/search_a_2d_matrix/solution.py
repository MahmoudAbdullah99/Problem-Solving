class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        
        while l <= r:
            m = (l+ r) // 2
            if target == matrix[m][0]:
                return True
            elif target > matrix[m][0]:
                l = m+1
            else:
                r = m-1
        
        row = r
        l, r = 0, len(matrix[row])-1
        
        while l <= r:
            m = (l+ r) // 2
            
            if target == matrix[row][m]:
                return True
            elif target > matrix[row][m]:
                l = m+1
            else:
                r = m-1
        
        return False