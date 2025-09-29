class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for c in s:
            if c in pair.values():
                stack.append(c)
            elif stack and stack[-1] == pair[c]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0