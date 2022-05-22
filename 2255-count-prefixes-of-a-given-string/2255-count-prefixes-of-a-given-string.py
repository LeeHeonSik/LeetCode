class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for w in words:
            if w == s[:len(w)]:
                ans += 1
        return ans