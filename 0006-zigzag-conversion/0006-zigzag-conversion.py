class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        arr = [] # i(top -> bottom) j(left -> right)
        count = 0
        I = 0
        J = 0

        k_I = 1
        k_J = 0

        while count < len(s):
            if I == 0:
                k_I = 1
                k_J = 0
            if I == numRows - 1:
                k_I = -1
                k_J = 1

            arr.append([I, J, s[count]])

            I += k_I
            J += k_J
            count += 1
            
        res = ''
        arr.sort()
        for i in arr:
            res += i[2]
        
        return res

