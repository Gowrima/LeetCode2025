class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            #print (c, stack)
            if c in pairs.keys():
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
            #print (c, stack)
            
        return len(stack) == 0
