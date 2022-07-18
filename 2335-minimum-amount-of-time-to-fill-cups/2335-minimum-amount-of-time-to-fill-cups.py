class Solution:
    def fillCups(self, a: List[int]) -> int:
        a = sorted(a)
        if a[2] > a[1] + a[0]:
            return a[2]
        else:
            k = (max(a[0] - (a[2] - a[1]), 0) + 1) // 2
            return a[2] + k