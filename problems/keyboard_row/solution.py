class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [{'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'},
                {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'},
                {'z', 'x', 'c', 'v', 'b', 'n', 'm',
                 'Z', 'X', 'C', 'V', 'B', 'N', 'M'}]
        
        ans = []
        for word in words:
            f = word[0]
            for i, row in enumerate(rows):
                if f in row:
                    n = i
                    break
                    
            if all(c in rows[n] for c in word):
                ans.append(word)
        
        return ans