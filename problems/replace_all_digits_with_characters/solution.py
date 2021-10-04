class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            if s[i].islower():
                ans += s[i]
            else:
                ans += chr(ord(s[i-1])+int(s[i]))
        return ans