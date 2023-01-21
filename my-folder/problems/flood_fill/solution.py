class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == 0:
            return image
        
        curr_color = image[sr][sc]
        
        def fill(sr,sc):
            if not 0 <= sr < len(image) or not 0 <= sc < len(image[0]) or image[sr][sc] != curr_color or image[sr][sc] == color:
                return
            
            image[sr][sc] = color

            fill(sr-1,sc)
            fill(sr+1,sc)
            fill(sr,sc-1)
            fill(sr,sc+1)
        
        fill(sr,sc)
        
        return image