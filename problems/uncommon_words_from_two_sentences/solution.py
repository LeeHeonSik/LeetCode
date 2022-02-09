class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        s = s1 + s2
        dic = Counter(s)
        ans = []
        for i, j in dic.items():
            if j == 1:
                ans.append(i)
        return ans
        