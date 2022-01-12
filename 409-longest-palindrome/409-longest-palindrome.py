class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = Counter(s)
        ans = 0
        for i in dic.values():
            ans += (i // 2) * 2
            if i % 2 == 1 and ans % 2 == 0:
                ans += 1
        return ans