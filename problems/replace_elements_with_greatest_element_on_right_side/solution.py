class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1 :
            return [-1]
        
        ans=[]
        for i in range(1,len(arr)):
            ans.append(max(arr[i:]))
        ans.append(-1)
        
        return ans