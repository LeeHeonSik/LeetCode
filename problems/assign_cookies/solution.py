class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        ans = 0
        
        while g and s:
            if s[-1] >= g[-1]:  
                s.pop()
                g.pop()
                ans += 1
            else:
                g.pop()
                
        return ans