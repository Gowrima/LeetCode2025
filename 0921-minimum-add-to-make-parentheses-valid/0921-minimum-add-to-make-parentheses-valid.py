class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_, close_ = 0, 0

        for c in s:
            if c == '(':
                open_ += 1
            elif open_ > 0:
                open_ -= 1
            else:
                close_ += 1
        
        return open_ + close_