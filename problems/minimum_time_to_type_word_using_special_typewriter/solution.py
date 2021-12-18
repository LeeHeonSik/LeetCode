class Solution:
    def minTimeToType(self, word: str) -> int:
        # alphabet list 2 times, using index
        
        s = 'a'
        ans = len(word)
        for i in word:
            k = abs(ord(i) - ord(s))
            if k > 13:
                k = 26 - k
            ans += k
            s = i
        
        return ans