class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic={}
        for i in arr:
            dic[i] = dic.get(i,0) + 1
        for j in dic:
            if dic[j] > len(arr)/4 :
                return j