class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
        
        sorted_freq = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        
        for i, count in enumerate(sorted_freq):

            cost = (i // 8) + 1
            total_pushes += count * cost
            
        return total_pushes