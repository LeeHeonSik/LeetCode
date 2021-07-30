class Solution:
    def climbStairs(self, n: int) -> int:
        count=0
        for i in range((n//2)+1):
            a=n-i*2
            b=(math.factorial(a+i) /(math.factorial(i) * math.factorial(a)))
            count+=b
        return int(count)