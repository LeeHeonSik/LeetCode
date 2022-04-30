class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for i, j in enumerate(s):
            if ans != []:
                if ans[-1] == j:
                    ans.pop()
                else:
                    ans.append(j)
            else:
                ans.append(j)
        return ''.join(ans)