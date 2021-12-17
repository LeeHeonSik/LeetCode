from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = Counter(arr)
        ans = []
        for i in dic.values():
            if i not in ans:
                ans.append(i)
            else:
                return False
        return True