class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if eval("*".join([j for j in str(n)])) % t == 0:
                return n
            n += 1