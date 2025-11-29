class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        expr = ['+', '-', '*', '/']
        a, b = 0, 0

        for token in tokens:
            if token in expr:
                if len(stack) > 1:
                    a = stack.pop()
                    b = stack.pop()  
                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(b-a)
                elif token == '*':
                    stack.append(a*b)
                elif token == '/':
                    stack.append(int(b/a))
            else:
                stack.append(int(token))
            
        return stack[0]