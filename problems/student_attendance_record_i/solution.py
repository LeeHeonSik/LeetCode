class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        for i in range(len(s)):
            if s[i] == 'A':
                a += 1
                if a == 2:
                    return False
            elif s[i] == 'L' and i >= 2:
                if s[i-1] == s[i-2] == 'L':
                    return False
        return True