class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        if S==0:
            return True
        k = 0
        for i in range(len(t)):
            if t[i] == s[k]:
                k += 1
                if S == k:
                    return True
        return False