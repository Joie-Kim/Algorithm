# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# 32 ms
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        
        return len(stack) == 0
