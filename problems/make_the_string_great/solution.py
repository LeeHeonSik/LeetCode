class Solution:
    def makeGood(self, s: str) -> str:
        for i in range(len(s) - 1):
            if (s[i] == s[i + 1].upper() or s[i].upper() == s[i + 1]) and (s[i].islower() or s[i + 1].islower()):
                return Solution.makeGood(self, s[:i] + s[(i + 2):]) 
        return s