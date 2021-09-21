class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dic = {'N' : 1, 'S' : -1, 'E' : 1, 'W' : -1}
        x,y = 0,0
        ans=[(0,0)]
        for i in path:
            if i == 'N' or i == 'S':
                y+= dic[i]
            elif i == 'E' or i == 'W':
                x+=dic[i]
            if (x,y) in ans:
                return True
            ans.append((x,y))
            
        return False