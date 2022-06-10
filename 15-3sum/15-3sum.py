class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res


# backtracking solution
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) < 3: return []
        
#         ans = []
        
#         def backtrack(lis, comb):
            
#             if len(comb) == 3:
#                 # print(comb)
#                 tmp = sorted(comb)
#                 if sum(tmp) == 0 and tmp not in ans:
#                     ans.append(tmp.copy())
#                 return
            
            
#             for i in range(len(lis)):
#                 comb.append(lis[i])
#                 backtrack(lis[i+1:], comb)
#                 comb.pop()
        
#         backtrack(nums, [])
        
#         return ans