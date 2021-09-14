class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dic = {}
        for i in range(len(words)):
            for j in words[i]:
                dic[j] = dic.get(j,0) +1
        for i in dic.keys():
            if dic[i]%len(words) !=0:
                return False
        return True