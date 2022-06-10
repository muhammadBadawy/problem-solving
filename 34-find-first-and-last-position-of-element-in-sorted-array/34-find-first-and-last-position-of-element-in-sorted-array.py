class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(l, r):
            
            if l == r:
                return
            
            mid = (l+r)//2
            
            if nums[mid] == target:
                for i in range(l, mid+1):
                    if nums[i] == target:
                        ans[0] = i
                        break
                for i in range(r-1, mid-1, -1):
                    if nums[i] == target:
                        ans[1] = i
                        break
                return
            elif nums[mid] < target:
                binarySearch(mid+1, r)
            elif nums[mid] > target:
                binarySearch(l, mid)
        
        ans = [-1, -1]
        
        binarySearch(0, len(nums))
        
        return ans