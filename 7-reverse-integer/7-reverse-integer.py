class Solution:
    def reverse(self, x: int) -> int:
        pos = True if x >= 0 else False
        compl = lambda x: -(10 - x) if x > 0 else 0
        
        result = 0
        
        while x != 0:
            result *= 10
            to_be_added = x % 10 if pos else compl(x % 10)
            result += to_be_added
            x = int(x/10)
        
        if result < -(2**31) or result > (2**31)-1:
            return 0
        else:
            return result