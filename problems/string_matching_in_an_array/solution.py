class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in words:
            for j in words:
                if i in j and i != j:
                    ans.append(i)
                    break
        return ans