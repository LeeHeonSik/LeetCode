class Solution:
    def isThree(self, n: int) -> bool:
        if n < 3:
            return False
        
        else:
            c = 0
            for i in range(2,n):
                if n % i == 0:
                    c += 1
                if c >= 2:
                    return False
            return c == 1