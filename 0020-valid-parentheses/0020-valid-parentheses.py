class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')':'(', '}':'{', ']':'['}
        stack = []

        for i in range(len(s)):
            if stack and s[i] in pair and stack[-1] == pair[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])
        
        return len(stack) == 0