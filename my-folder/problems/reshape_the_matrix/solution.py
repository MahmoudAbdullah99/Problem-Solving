class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        raw_mat = []
        reshaped_mat = []
        
        for row in mat:
            raw_mat.extend(row)
        
        if len(raw_mat) / r != c:
            return mat
        
        for i in range(0, len(raw_mat), c):
            reshaped_mat.append(raw_mat[i:i+c])

        return reshaped_mat