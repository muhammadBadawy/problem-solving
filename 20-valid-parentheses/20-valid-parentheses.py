class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1: return False
        valid = [("(",")"),("[","]"),("{","}")]
        stack = []
        
        for char in s:
            stack.append(char)
            if len(stack) >= 2 and (stack[-2], stack[-1]) in valid:
                stack.pop()
                stack.pop()
        # print(stack)
        
        if stack:
            return False
        else:
            return True