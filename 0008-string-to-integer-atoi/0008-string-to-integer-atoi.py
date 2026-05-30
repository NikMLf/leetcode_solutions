class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if len(s) == 0:
            return 0
        def f(x):
            if x == '-' or x == '+':
                return 0
            x = int(x)
            return max(-2**31, min(x, 2**31-1))
        
        res = ''
        if s[0] == '-' or s[0] == '+':
            res += s[0] 
            s = s[1:]
        
        for i in s:
            if i not in '0123456789':
                return f(res) if len(res) != 0 else 0
            res += i

        return f(res)