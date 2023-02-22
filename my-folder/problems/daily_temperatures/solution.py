class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for indx, element in enumerate(temperatures):
            while stack and element > stack[-1][1]:
                stack_top_indx, stack_top = stack.pop()
                res[stack_top_indx] = indx-stack_top_indx
            
            stack.append((indx, element))
        
        return res