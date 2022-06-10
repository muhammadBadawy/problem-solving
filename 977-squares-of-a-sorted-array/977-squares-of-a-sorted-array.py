class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)-1
        
        l = 0
        r = i = length
        # result = []
        result = [None]*len(nums)
        
        while l <= r:
            if abs(nums[r]) >= abs(nums[l]):
                # result = [nums[r]**2] + result
                # result.append(nums[r]**2)
                result[i] = nums[r]**2
                i-=1
                r-=1
            else:
                # result = [nums[l]**2] + result
                # result.append(nums[l]**2)
                result[i] = nums[l]**2
                i-=1
                l+=1
        
        return result