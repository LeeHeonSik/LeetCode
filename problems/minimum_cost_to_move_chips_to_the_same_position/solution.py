from collections import Counter
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd, even = 0 ,0
        p = Counter(position)
        for i in p:
            if i % 2 == 0:
                even += p[i]
            else:
                odd += p[i]
        return min(odd, even)
        