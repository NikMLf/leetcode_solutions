class Solution:
    def grayCode(self, n: int) -> List[int]:
        total = 1 << n  # 2^n
        result = []
        for i in range(total):
            # Formula: G(i) = i ^ (i >> 1)
            result.append(i ^ (i >> 1))
        return result