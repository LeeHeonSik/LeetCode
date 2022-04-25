class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        st, end = 0, len(colors) - 1
        n = end
        while colors[st] == colors[end]:
            st += 1
        while colors[0] == colors[end]:
            end -= 1
        return max(n-st, end)