class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = {}
        for p in paths:
            dic[p[0]] = dic.get(p[0],0) + 1
            dic[p[1]] = dic.get(p[1], 0) + 100
        for i, j in dic.items():
            if j == 100:
                return i
        return paths[0][1]