class Solution:
    def maxPower(self, s: str) -> int:
        count=0
        k=0
        M=0
        for i in s:
            if i == k:
                count+=1
            else:
                k=i
                count=1
            M=max(M,count)
        return M