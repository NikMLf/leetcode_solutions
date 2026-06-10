class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 0
        if dividend == -2147483648 and divisor == -1:
            return 2147483647 
        if dividend == 0:
            return 0
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        result = 0
        while dvd >= dvs:
            shift = 0
            while dvd >= (dvs << (shift + 1)):
                shift += 1
            
            result += 1 << shift
         
            dvd -= dvs << shift
        

        result *= sign

        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result   