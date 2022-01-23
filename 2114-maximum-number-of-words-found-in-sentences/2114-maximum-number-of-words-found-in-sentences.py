class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 1
        for i in sentences:
            c = 1
            for j in i:
                if j == " ":
                    c += 1
            if c > ans:
                ans = c
        
        return ans