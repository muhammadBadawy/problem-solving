# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         result = []
#         list_size = len(nums)
#         for i in range(list_size):
#             for y in range(i+1, list_size):
#                 if nums[i] + nums[y] == target:
#                     result.append(i)
#                     result.append(y)
#         return result

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        list_size = len(nums)
        i = 0
        while i < list_size:
            y = i+1
            while y < list_size:
                if nums[i] + nums[y] == target:
                    result.append(i)
                    result.append(y)
                y+=1
            i+=1
        return result