class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(o, c, s):
            if o == c == n:
                res.append(s)
                return
            
            if o > c:
                generate(o, c+1, s+')')
            
            if o < n:
                generate(o+1, c, s+'(')
                        
        generate(1, 0, '(')

        return res