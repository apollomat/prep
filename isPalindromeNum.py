class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0):
            return False
        if(x <= 9):
            return True
        if(x% 10 == 0):
            return False
        y = 0
        
        while (x > y):
            y *= 10
            y += x%10
            
            x = x / 10
        return x == y or y/10==x
            
