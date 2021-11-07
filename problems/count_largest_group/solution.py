class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = {}
        for i in range(1,n+1):
            c = 0
            for j in str(i):
                c += int(j)
            dic[c] = dic.get(c,0) + 1
            
        C = Counter(dic.values())
        return C[max(C)]