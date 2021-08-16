class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = str(bin(n))
        if all(n[a] != n[a+1] for a in range(len(n)-1)):
            return True
        return False