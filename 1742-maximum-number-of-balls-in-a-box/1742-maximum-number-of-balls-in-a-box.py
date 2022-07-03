class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dic = {}
        for i in range(lowLimit, highLimit+1):
            k = str(i)
            t = 0
            for kk in k:
                t += int(kk)
            if t in dic.keys():
                dic[t] += 1
            else:
                dic[t] = dic.get(t,0) + 1
        return max(dic.values())