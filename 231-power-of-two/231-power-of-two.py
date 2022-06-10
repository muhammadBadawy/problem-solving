class Solution:
    def isPowerOfTwo(self, n):
        tmp = 1
        
        while tmp <= n:
            if tmp == n:
                return True
            tmp*=2
        
        return False