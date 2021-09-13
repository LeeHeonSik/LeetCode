class Solution:
    def tribonacci(self, n: int) -> int:
        _sum = [0,1,1]
        if n == 0:
            return _sum[0]
        if n ==1 or n ==2 :
            return _sum[1]
        if n >=3:
            for i in range(3,n+1):
                k = sum(_sum[i-3:i])
                _sum.append(k)
        return _sum[-1]