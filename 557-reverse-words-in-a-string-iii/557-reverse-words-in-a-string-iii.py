class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = ""
        for i in range(len(s)):
            ans += s[i][::-1]
            ans += " "
        return ans[:-1]