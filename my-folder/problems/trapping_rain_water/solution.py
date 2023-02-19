class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left, right = 0, len(height)-1
        
        max_left, max_right = height[left], height[right]
        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                area += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                area += max_right - height[right]


        return area
                                                