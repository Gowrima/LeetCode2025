class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generateParenthesis_helper(soFar, open, close, paren=[]):
            if not open and not close:
                paren.append(soFar)

            if open:
                generateParenthesis_helper(soFar+'(', open-1, close)
            
            if close>open:
                generateParenthesis_helper(soFar+')', open, close-1)

            return paren
        
        return generateParenthesis_helper('', n, n)