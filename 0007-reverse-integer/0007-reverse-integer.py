class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 10 and x > -10:
            return x

        res = ''
        sign = ''
        if x < 0:
            sign = '-'
            x = str(x)[1:]
        x = str(x)

        for i in range(1, len(x)+1):
            res += x[-i]
        
        while x[0] == '0':
            x.replace('0', '', 1)

        res = int(sign + res)

        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
    