from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dic = Counter(sentence)
        
        for i in range(97, 123):
            if chr(i) not in dic.keys():
                return False
        return True