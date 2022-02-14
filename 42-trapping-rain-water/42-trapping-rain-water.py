class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        le = 0
        ri = 0
        
        for i in range(len(height)):
            
            if le <= height[i]:
                le = height[i]
                
            else:
                ri = max(height[i::])
                ans += min(le, ri) - height[i]
                
        return ans