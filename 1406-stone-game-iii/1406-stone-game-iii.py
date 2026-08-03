from typing import List
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
    
        dp = [0] * (n + 1)
    
        for i in range(n - 1, -1, -1):
            take = 0
            best_diff = float('-inf')
            for k in range(1, 4):
                if i + k - 1 < n:
                    take += stoneValue[i + k - 1]
    
                    best_diff = max(best_diff, take - dp[i + k])
                else:
                    break
            
            dp[i] = best_diff
    
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
    