class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        le = 0
        
        for i in range(len(height)):
            ri = 0
            le = max(le, height[i])
            
            if le != height[i]:
                ri = max(height[i::])
                ans += min(le, ri) - height[i]
                
        return ans