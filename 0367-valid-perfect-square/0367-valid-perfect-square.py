class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        
        left = 2
        right = num/2
        
        while left <= right:
            mid = (left+right)/2
            tmp = mid*mid
            if tmp == num:
                return True
            elif tmp > num:
                right = mid-1
            else:
                left = mid+1
            
        return False
                
        