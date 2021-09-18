class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        reverse = s[::-1]
        for i, j in enumerate(s):
            if reverse[i] != j:
                reverse = reverse[ : i] + reverse[i + 1:]
                if reverse == reverse[::-1]:
                    return True
                s = s[0:i] + s[i+1:]
                return s == s[::-1] 