class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count = []
        for i in range(len(mat)):
            c = mat[i].count(1)
            count.append([i,c])
        ans = sorted(count, key = lambda x : x[1])
        return [ans[i][0] for i in range(k)]