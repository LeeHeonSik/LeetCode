from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = Counter(arr)
        ans = -1
        for i in dic:
            if i == dic[i]:
                if ans < i:
                    ans = i
        return ans
        
        