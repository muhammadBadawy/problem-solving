class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        s_length = len(s)
        if s_length <= 0:
            return ""
        
        start = 0
        end = 0
        i = 0
        
        while i < s_length:
            even_len = self.expandAroundCenter(s, i, i)
            odd_len = self.expandAroundCenter(s, i, i+1)
            
            length = max(even_len, odd_len)
            
            if length > end - start:
                start = i - (length - 1)//2
                end = i + (length//2) + 1
                
            i+=1
        return s[start:end]
    
    def expandAroundCenter(self, s: str, l: int, r: int) -> bool:
        length = len(s)
        
        while l >= 0 and r < length and s[r] == s[l]:
            l-=1
            r+=1
        
        return r - l - 1
