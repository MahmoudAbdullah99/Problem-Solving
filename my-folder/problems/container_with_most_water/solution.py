class Solution:
    # def bruteForceMaxArea(self, height: List[int]) -> int:
    #     max_area = 0
    #     for i, h_i in enumerate(height):
    #         for  j, h_j in enumerate(height[i+1:]):
    #             temp_area = ((j-i) * min(height[i], height[j]))
    #             max_area = max(temp_area, max_area)
    #     return max_area
    
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_area = 0
        while i < j:
            temp_area = ((j-i) * min(height[i], height[j]))
            max_area = max(temp_area, max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area