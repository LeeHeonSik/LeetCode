class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        k = ''.join(x for x in s if x.isalpha())[::-1]
        ans = ""
        c = 0
        for i in range(len(s)):
            if s[i].isalpha():
                ans += k[c]
                c += 1
            else:
                ans += s[i]
        return ans