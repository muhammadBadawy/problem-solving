class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def rev(arr, l, r):
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
                r-=1
                
        length = len(nums)
        k = k % length
        
        rev(nums, 0, length-1)
        rev(nums, 0, k-1)
        rev(nums, k, length-1)