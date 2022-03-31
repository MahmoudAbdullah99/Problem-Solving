class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        currentColor = image[sr][sc]

        def fill(sr, sc):
            
            if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] == newColor or image[sr][sc] != currentColor:
                    return
            
            image[sr][sc] = newColor
            
            fill(sr+1, sc)
            fill(sr-1, sc)
            fill(sr, sc+1)
            fill(sr, sc-1)
        
        if image[sr][sc] == newColor:
            return image
        
        fill(sr, sc)
        
        return image

