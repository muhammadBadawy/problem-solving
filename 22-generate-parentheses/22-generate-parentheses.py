class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(l, r, comb):
            
            if l == 0 and r == 0:
                res.append("".join(comb))
                return
            
            if l > 0:
                comb.append("(")
                backtrack(l-1, r, comb)
                comb.pop()
            if r > l:
                comb.append(")")
                backtrack(l, r-1, comb)
                comb.pop()
            
        
        backtrack(n,n,[])
        return res