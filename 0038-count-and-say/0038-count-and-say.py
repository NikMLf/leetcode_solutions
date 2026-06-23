class Solution:
    def countAndSay(self, n: int) -> str:

        result = "1"
        
        for _ in range(n - 1):
            next_term = []
            count = 1
            
            for i in range(len(result)):

                if i + 1 < len(result) and result[i] == result[i+1]:
                    count += 1
                else:

                    next_term.append(f"{count}{result[i]}")
                    count = 1
      
            result = "".join(next_term)
        
        return result