class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(14,-1,-1):
            if n >= 3**i:
                n -= 3**i
            if n < 0:
                return False
            elif n == 0:
                return True