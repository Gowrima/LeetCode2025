class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
            