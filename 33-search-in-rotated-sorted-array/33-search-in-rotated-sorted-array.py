class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        def binarySearch(l,r):
            mid = (l+r)//2
            
            if l > r:
                return
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[r]:
                
                # we need the = here cuz at some point the list will
                # be reduced to a list with one element
                # so we need to compare the target with that single element
                # also because they may be equals!, and we need to check on that
                if nums[mid] <= target <= nums[r]:
                    return binarySearch(mid+1, r)
                else:
                    return binarySearch(l, mid-1)
            else:
                if nums[l] <= target <= nums[mid]:
                    return binarySearch(l, mid-1)
                else:
                    return binarySearch(mid+1, r)
        
        result = binarySearch(0, len(nums)-1)
        
        return result if result is not None else -1