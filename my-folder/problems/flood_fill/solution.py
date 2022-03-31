class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        currentColor = image[sr][sc]
        rows, cols = len(image), len(image[0])

        def fill(sr, sc, currentColor):
            
            if sr < 0 or sc < 0 or sr > rows-1 or sc > cols-1 or image[sr][sc] == newColor or image[sr][sc] != currentColor:
                    return
            
            image[sr][sc] = newColor
            fill(sr-1, sc, currentColor)
            fill(sr+1, sc, currentColor)
            fill(sr, sc-1, currentColor)
            fill(sr, sc+1, currentColor)
        
        
        fill(sr, sc, image[sr][sc])
        
        return image
            
        