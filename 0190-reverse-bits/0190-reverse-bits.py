class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = bin(n)[2:]
        bin_n = '0' * (32-len(bin_n)) + bin_n
        bin_n = ''.join([bin_n[i] for i in range(len(bin_n) - 1, -1, -1)])
        return int(bin_n, 2)