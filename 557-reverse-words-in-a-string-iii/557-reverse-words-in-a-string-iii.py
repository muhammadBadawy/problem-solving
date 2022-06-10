class Solution:
    def reverseWords(self, s: str) -> str:
        
        left, right = 0, 0
        res = []
        while right < len(s):
            if s[right] == ' ':
                cur_word = s[left:right]
                res.append(cur_word[::-1])
                left = right + 1
        
            right += 1
        
        res.append(s[left:right][::-1])
        
        return " ".join(res)