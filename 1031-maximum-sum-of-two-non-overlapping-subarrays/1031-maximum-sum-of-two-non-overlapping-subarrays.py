class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], f: int, s: int) -> int:
        if f < s:
            f , s = s , f
        ans = 0
        
        for i in range(len(A) - f + 1):
            temp1 = sum(A[i:i+f])
   
            if i >= s:
                for j in range(i - s + 1):
                    t2 = sum(A[j:j+s])
                    ans = max(ans,temp1 + t2)

            if len(A)-i-f >= s:
                for j in range(i+f, len(A)):
                    t2=sum(A[j:j+s])
                    ans=max(ans, temp1+t2)
        return ans