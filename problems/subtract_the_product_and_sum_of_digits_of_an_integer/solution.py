class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        d = 1
        s = 0
        for i in n:
            d *= int(i) 
            s += int(i)
        return d - s