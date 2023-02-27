class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        
        for indx, height in enumerate(heights):
            st_indx = indx
            while stack and height < stack[-1][1]:
                st_indx, area = stack.pop()
                max_area = max(area * (indx-st_indx), max_area)
            
            stack.append((st_indx,height))
        
        for indx, area in stack:
            max_area = max(area * (len(heights) - indx), max_area)
        
        return max_area