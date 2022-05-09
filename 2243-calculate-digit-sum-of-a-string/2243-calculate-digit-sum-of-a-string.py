class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            temp = []
            ave = ""
            for i in range(0, len(s), k):
                temp.append(s[i:i+k])
            for t in temp:
                q = [int(a) for a in t]
                ave += str(sum(q))
            s = ave
        return s