class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            s = word.index(ch)
            
            word = word[s::-1] + word[s+1::]
        
        return word