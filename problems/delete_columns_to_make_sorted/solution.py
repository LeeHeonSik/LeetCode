class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for j in range(len(strs[0])):
            k=[]
            for i in range(len(strs)):
                k.append(strs[i][j])
            s = sorted(k)
            if s != k :
                ans+=1
        return ans