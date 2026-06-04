class Solution(object):
    def romanToInt(self, s):
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
        total = 0
        n = len(s)
        for i in range(n):
            current_value = values[s[i]]
            next_value = values[s[i+1]] if i + 1 < n else 0
            if current_value < next_value:
                total -= current_value
            else:
                total += current_value

        return total