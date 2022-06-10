class Solution:
    def climbStairs(self, n):
        if n == 0: return 0
        if n == 1: return 1
        dic = {
            0:0,
            1:1
        }
        
        # here we started at 2 because if we started at n=0, we cant calculate the n-1 and n-2 
        for i in range(2, n+2):
            dic[i] = dic[i-1]+dic[i-2]
            if i == n+1:
                return dic[i]
            
        print(dic)
        
        