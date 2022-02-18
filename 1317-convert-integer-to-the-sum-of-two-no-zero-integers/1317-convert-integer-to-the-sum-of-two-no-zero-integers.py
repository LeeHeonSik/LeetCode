class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        A = 1
        while A < n:
            if '0' not in str(A) + str(n-A):
                break
            A += 1
        return [A,n-A]