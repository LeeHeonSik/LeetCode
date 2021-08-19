class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0 :
            return False
        x = [2,3,5,6,10]
        for i in x:
            while n % i == 0:
                n = n / i
        if n == 1:
            return True
        else:
            return False