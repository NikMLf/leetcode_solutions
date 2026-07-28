class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        
        freq = Counter(s)
        
        first_half = []
        middle_char = ""
        
        for char in sorted(freq.keys()):
            count = freq[char]
            if count % 2 == 1:
            
                middle_char = char
    
            first_half.append(char * (count // 2))
        
        
        half_str = "".join(first_half)
    
        result = half_str + middle_char + half_str[::-1]
        
        return result