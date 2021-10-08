class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        a,k = 0,0
        ans = []
    
        if s1 == s2:
            return True
        
        for i, j in zip(s1,s2):
            if i != j:
                a +=1
                ans.append([i,j])
            if a >= 3:
                return False
        if a == 2:
            if ans[0] == ans[1][::-1]:
                return True
        else:
            return False