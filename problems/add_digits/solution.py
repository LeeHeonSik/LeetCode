class Solution:
    def addDigits(self, num: int) -> int:
        l = str(num)
        n = len(l)
        while n >1:
            s = 0
            for i in l:
                s += int(i)
            l = str(s)
            n = len(l)
        return l