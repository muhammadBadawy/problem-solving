class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = r = 0
        ans = 0
        hist = {}
        
        while r < len(s):
            if s[r] in hist:
                # here we make l point to the the most recent time s[r] was
                # dicovered by r, but what if l is already pointing to the most
                # recent time of s[r]?, then it should stay where it is.
                # like when we do "abba" at the last iteration, a exist in hist dict at point 0,
                # so l is gonna go back to 0, bet we tell l either you move forward or stay the same
                # and l is still 2
                l = max(hist[s[r]] + 1, l)
            
            ans = max(ans, r-l+1)
            hist[s[r]] = r
            r+=1
        
        return ans