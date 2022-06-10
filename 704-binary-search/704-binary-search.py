class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums)-1, target)
    
    def binarySearch(self, nums: List[int], low: int, high: int, target: int) -> int:
        
        middle_index = (low+high) // 2
        
        if nums[middle_index] == target:
            return middle_index
        elif low >= high:
            return -1
        elif target > nums[middle_index]:
            return self.binarySearch(nums, middle_index+1, high, target)
        elif target < nums[middle_index]:
            return self.binarySearch(nums, low, middle_index-1, target)
        # else:
        #     return -1