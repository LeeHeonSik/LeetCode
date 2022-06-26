class Solution:
    def greatestLetter(self, s: str) -> str:
        k = set(s)
        ans = ''
        for a in k:
            if a.lower() in k and a.upper() in k:
                ans = max(ans, a)
        return ans.upper()