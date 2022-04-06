class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        k = [i for i in range(start,start+2*n,2)]
        c = k[0]
        for i in range(1,len(k)):
            c = c^k[i]
        return c