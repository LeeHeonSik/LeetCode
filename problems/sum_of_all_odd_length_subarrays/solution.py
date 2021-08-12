class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        L = len(arr)
        arr_len = len(arr)
                
        if L % 2 == 0:
            L -= 1
        
        ans=[]
        for i in range(1, L+1, 2):
            for j in range(arr_len - i + 1):
                ans.append(sum(arr[j:j+i]))
        
        return sum(ans)