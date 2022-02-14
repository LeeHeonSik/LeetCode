class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        le, ri = height[i], height[j]
        ans = 0
        while i < j:
            if le > ri:
                j -= 1
                if height[j] > ri:
                    ri = height[j]
                else:
                    ans += ri - height[j]
            else:
                i += 1
                if height[i] > le:
                    le = height[i]
                else:
                    ans += le - height[i]
        return ans