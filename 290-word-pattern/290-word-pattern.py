class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        dic = dict()
        k = []
        for x, y in enumerate(s):
            if y in dic:
                if dic[y] != pattern[x]:
                    return False
            else:
                if pattern[x] in k:
                    return False
            dic[y] = pattern[x]
            k.append(pattern[x])
        return True