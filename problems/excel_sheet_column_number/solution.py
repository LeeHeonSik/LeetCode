class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        c = columnTitle[::-1]
        for i in range(len(c)):
            ans += (26**i)*(ord(c[i])-64)
        return ans