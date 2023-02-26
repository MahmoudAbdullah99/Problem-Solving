class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for indx, element in enumerate(temperatures):
            while stack and element > stack[-1][1]:
                res[stack[-1][0]] = indx - stack[-1][0]
                stack.pop()
            stack.append((indx, element))
        
        return res