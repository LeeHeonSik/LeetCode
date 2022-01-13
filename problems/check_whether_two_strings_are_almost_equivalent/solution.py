class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        dic1 = Counter(word1)
        dic2 = Counter(word2)
        dic = dic1 + dic2
        
        for i in dic:
            if i in dic1 and i in dic2:
                if abs(dic1[i] - dic2[i])> 3:
                    return False
            else:
                if (i in dic1 and dic1[i] > 3):
                    return False
                elif (i in dic2 and dic2[i] > 3):
                    return False
        return True