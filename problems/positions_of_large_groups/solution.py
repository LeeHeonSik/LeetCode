class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        k=0
        ans=[]
        for i in range(len(s)):
            if i == len(s)-1 or s[i] != s[i+1]:
                if i-k+1 >=3:
                    ans.append([k,i])
                k = i +1
        return ans