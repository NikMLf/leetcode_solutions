class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for i in [" ", ",", ".", ":", "/", "*", "@", "#", "_", "'", "[", "]", "{", "}", '"', "-", "!", "?", ";", "\\","(", ")", "`"]:
            s = s.replace(i, '') 
        _s = [i for i in s]
        s_ = _s.copy()
        _s.reverse()
        return _s == s_
