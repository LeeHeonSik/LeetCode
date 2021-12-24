class Solution: 
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        for i in range(len(mat)):
            if sum(mat[i])==1 :
                j=mat[i].index(1)
                col=[row[j] for row in mat]
                if sum(col)==1:
                    ans+=1
        
        return ans