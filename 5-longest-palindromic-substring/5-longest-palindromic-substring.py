class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        c = 0
        while c in range(len(s)):
            e = c 
            while e < len(s) - 1:
                if s[e + 1] == s[e]:
                    e += 1
                else: 
                    break

            t = 0
            while (c - t) > 0 and (e + t) < len(s) - 1: 
                if s[c - t - 1] == s[e + t + 1]:
                    t += 1
                else:
                    break

            if (e + t + 1) - (c - t) > len(ans): 
                ans = s[(c - t):(e + t + 1)]

            c = e + 1
        return ans