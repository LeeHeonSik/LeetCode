class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ans = 0
        dic1 = collections.Counter(words1)
        dic2 = collections.Counter(words2)
        for i in dic1.keys():
            if dic1[i] == 1:
                if i in dic2.keys() and dic2[i] == 1:
                    ans += 1
        return ans