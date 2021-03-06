class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            if n % 2 == 1:
                return False
            n = n // 2
        return n == 1