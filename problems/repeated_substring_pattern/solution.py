class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        c = len(s)
        if c ==1:
            return False
        if c == 2:
            return s[0] == s[1]
        
        for i in range(1,c//2 +1):
            if (c%i == 0) and s[:i] * (c//i) == s:
                return True
        return False