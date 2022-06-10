class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        last_zero_pos = 0
        i = 0
        
        while i < length:
            if nums[i] != 0:
                nums[i], nums[last_zero_pos] = nums[last_zero_pos], nums[i]
                last_zero_pos+=1
            i+=1
            