class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        c = ""
        t = 0
        for i in range(len(s)):
            if t == 0:
                ans += 1
                c = s[i]
                t += 1
            elif s[i] == c:
                t += 1
            else:
                t -= 1
        return ans