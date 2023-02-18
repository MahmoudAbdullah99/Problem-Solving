class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'(':')', '[':']', '{':'}'}
        for char in s:
            if parentheses.get(char):
                stack.append(char)
            elif len(stack) >= 1 and char == parentheses[stack[-1]]:
                stack.pop()
            else:
                return False
        if len(stack) > 0:
            return False
        
        return True
