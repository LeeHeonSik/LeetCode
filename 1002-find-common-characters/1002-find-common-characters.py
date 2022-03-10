class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        dic = collections.Counter(words[0])
        
        for i in words[1::]:
            for x, y in dic.items():
                if x in i:
                    dic[x] = min(y, i.count(x))
                else:
                    dic[x] = 0
        for k,v in dic.items():
            ans.extend([k]*v)
        return ans