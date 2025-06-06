class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        num = x

        while num > 0:
            reverse = (num % 10) + (reverse * 10)
            num = num//10
        
        return reverse == x
        