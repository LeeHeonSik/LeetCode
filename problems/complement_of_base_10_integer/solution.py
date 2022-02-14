class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(bin(n)[2::].replace('1','a').replace('0','1').replace('a','0'),2)
        