class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        r = len(s)
        s = list(s)
        
        def backtrack(l, r):
            if l == r:
                res.append("".join(s))
                return
            
            
            if s[l].isalpha():
                backtrack(l+1, r)
                s[l] = s[l].swapcase()
                backtrack(l+1, r)
                s[l] = s[l].swapcase()
            else:
                backtrack(l+1, r)
        
        backtrack(0, r)
        
        return res