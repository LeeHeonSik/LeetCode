class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        le = 0
        fstmax = max(height)
        idx = height.index(fstmax)
        
        for i in range(len(height)):
            ri = 0
            
            if le <= height[i]:
                le = height[i]
                
            else:
                if i < idx:
                    ans += min(le, fstmax) - height[i]
                else:
                    ri = max(height[i::])
                    ans += min(le, ri) - height[i]
                
        return ans