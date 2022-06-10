class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(1, len(matrix)):
            matrix[0] += matrix[i]
        
        matrix = matrix[0]
        
        def binarySearch(l,r):
            mid = (l+r)//2
            
            if l > r:
                return None
            
            if matrix[mid] == target:
                return True
            
            if target < matrix[mid]:
                return binarySearch(l, mid-1)
            else:
                return binarySearch(mid+1, r)
        
        ans = True if binarySearch(0, len(matrix)-1) is not None else False
        return ans
            