class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = list(range(1, n+1))
        
        def backtrack(arr, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for i in range(len(arr)):
                comb.append(arr[i])
                backtrack(arr[i+1:], comb)
                comb.pop()
        
        backtrack(nums, [])
        return res