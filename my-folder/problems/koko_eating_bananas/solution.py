class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed, max_speed = 1, max(piles)
        res = max_speed
        
        while min_speed <= max_speed:
            mid_speed = (min_speed + max_speed) // 2
            temp_h = 0
            
            for p in piles:
                temp_h += ceil(p/mid_speed)
            
            if temp_h > h:
                min_speed = mid_speed+1
            
            else:
                res = min(res, mid_speed)
                max_speed = mid_speed-1
        
        return res