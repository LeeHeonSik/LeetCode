class Solution:
    def checkString(self, s: str) -> bool:
        s = list(s)
        k = sorted(s)
        return s == k