class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n):
            if '0' in str(i):
                continue
            if '0' in str(n-i):
                continue
            ans=[i,n-i]
            return ans