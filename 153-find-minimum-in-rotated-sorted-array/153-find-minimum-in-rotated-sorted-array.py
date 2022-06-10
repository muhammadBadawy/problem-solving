class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def binarySearch(l, r):
            
            mid = (l+r)//2
            
            if l == r:
                return nums[l]
            
            # since whenever the rotation happens, the data moves right
            # so the bigger values goes to the left, and the max value
            # moves inside the lisst, So we know that if the value in the middle
            # is greather than the one at the last, then the min is in the right side
            # else, it means the max value that was at the end of the list haven't
            # reached the mid, and the min syill in the left side
            if nums[mid] > nums[r]:
                # note that here we didn (mid+1, r)
                # cuz if the result is reduced to list with 2 values
                # and the first is greater than the second
                # knowing that the first element is 0 and the second is 1
                # r = 1 and mid = 0, if we will take (mid, r) then
                # we will get (0, 1) and thats not we want, we want (1, 1)
                return binarySearch(mid+1, r)
            else :
                # note that here we didn't do (l, mid-1)
                # cuz if the result is reduced to list with 2 values
                # and the first is smaller than the second
                # knowing that the first element is 0 and the second is 1
                # l = 0 and mid = 0, if we will take (l, mid-1) then
                # we will get (0, -1) and thats not we want, we want (0, 0)
                return binarySearch(l, mid)
            
        return binarySearch(0, len(nums)-1)