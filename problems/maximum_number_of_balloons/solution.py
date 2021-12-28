from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = 'balloon'
        dic2 = Counter(text)
        ans = []
        for i in s:
            if i in dic2.keys():
                ans.append(dic2[i])
                dic2[i] = dic2[i] // 2
            else:
                return 0
            
        return min(ans)