class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        k = [9,9,8,7,6,5,4,3,2,1]
        ans,t=1,1
        for i in range(n):
            t*=k[i]
            ans+=t
        return ans