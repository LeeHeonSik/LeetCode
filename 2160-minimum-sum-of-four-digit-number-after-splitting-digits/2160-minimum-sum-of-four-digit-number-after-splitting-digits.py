class Solution:
    def minimumSum(self, num: int) -> int:
        k = []
        num = str(num)
        for i in num:
            k.append(i)
        k.sort()
        
        return int(k[0] + k[2]) + int(k[1] + k[3])