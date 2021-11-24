from collections import Counter
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = Counter(s)
        if all(i==1 for i in dic.values()):
            return -1
        
        c = 0
        for i in dic.keys():
            k = len(s) - (s.index(i)+ s[::-1].index(i)+2)
            if  k > c:
                c = k
        return c
                