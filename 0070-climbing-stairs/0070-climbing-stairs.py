class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <=2:
            return n
         
        first = 1
        second = 2
        
        while n > 2:
            th = first+second
            first, second = second, th
            n -= 1
            
        return second
            