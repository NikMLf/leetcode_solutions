class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if -2**31 > x or x > 2**31 - 1:
            return False
        
        return int(''.join([str(x)[-i] for i in range(1, len(str(x))+1)])) == x