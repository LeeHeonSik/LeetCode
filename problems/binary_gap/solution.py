class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        b = str(bin(n))
        c = 0
        for i in b[2::]:
            if i == '1':
                if ans < c:
                    ans = c
                c = 0
            c += 1
        return ans