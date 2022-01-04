from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = Counter(s)
        n = dic[s[0]]
        for i in dic.values():
            if i != n:
                return False
        return True