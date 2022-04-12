class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = 0
        m = max(arr)
        for i in range(1,m+1):
            if i not in arr:
                ans += 1
            if ans == k:
                return i
        return (k-ans) + m