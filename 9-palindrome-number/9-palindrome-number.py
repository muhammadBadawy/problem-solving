class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        
        original_x = x
        result = 0
        while x > 0:
            result *= 10
            result += x%10
            x = int(x/10)
        return result == original_x