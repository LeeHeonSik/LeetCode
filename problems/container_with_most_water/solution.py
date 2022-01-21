class Solution:
    def maxArea(self, height: List[int]) -> int:
        M, x= 0, 0
        b = len(height)-1
        
        while x != b:
            if height[b] > height[x]:
                s = height[x] * (b - x)
                x += 1
            else:
                s = height[b] * (b - x)
                b -= 1
                
            M = max(M, s)
            
        return M