class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        s = list(s)
        c = sorted(s)
        d = sorted(s, reverse = True)
        if s != c and s != d:
            return False
        return True