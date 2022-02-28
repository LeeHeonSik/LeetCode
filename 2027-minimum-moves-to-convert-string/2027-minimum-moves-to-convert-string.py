class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = 0
        s = list(s)
        for i in range(len(s)-2):
            if s[i] == 'X':
                s[i] = 'O'
                s[i+1] = 'O'
                s[i+2] = 'O'
                ans += 1
        if s[-1] == 'X' or s[-2] == 'X':
            ans += 1
        return ans