class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = sorted(list(zip(position, speed)))
        
        for curr_pos, curr_speed in pos_speed:
            finish_time = (target - curr_pos) / curr_speed
            
            while stack and finish_time >= stack[-1]:
                stack.pop()
            
            stack.append(finish_time)
        
        return len(stack)
