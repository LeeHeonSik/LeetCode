class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if trust == []:
            if n == 1:
                return 1
            else : return -1
        ans = {}
        p = {}
        for i in trust:
            ans[i[1]] = ans.get(i[1], 0) + 1
            ans[i[0]] = ans.get(i[0], 0) - 1

        ans = sorted(ans.items(), key = lambda item: item[1], reverse = True)
        
        if ans[0][1] == n-1:
            return ans[0][0]
        else: return -1