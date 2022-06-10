class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # if len(nums) <= 2: return nums.index(max(nums))
        
        def isPeak(i):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return True
            return False
        
        def binarySearch(l, r):
            if l == r:
                return l
            
            mid = (l+r)//2
            
            if isPeak(mid):
                 return mid
            
            # here i used to do if nums[mid-1] < nums[mid+1]:
            # but this messed up with lists with 2 elemnts only
            # so please take care of the lists with 2 elements
            if nums[mid] < nums[mid+1]:
                return binarySearch(mid+1, r)
            else:
                return binarySearch(l, mid-1)
            
            
        return binarySearch(0, len(nums)-1)