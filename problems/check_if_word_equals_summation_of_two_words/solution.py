class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        
        fw, sw, tg= '', '', ''
        
        for i in firstWord:
            fw += str(dic.index(i))
        for j in secondWord:
            sw += str(dic.index(j))
        for k in targetWord:
            tg += str(dic.index(k))
        
        return (int(fw) + int(sw)) == int(tg)