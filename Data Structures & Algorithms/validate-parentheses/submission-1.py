class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {
            '}': '{',
            ']': '[',
            ')': '(',
        }
        stack = []
        for char in s:
            if char in paren_map:
                top = stack.pop() if stack else '#'
                if paren_map[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack