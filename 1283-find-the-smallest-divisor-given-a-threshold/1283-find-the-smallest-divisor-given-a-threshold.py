class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(mid):
            ans = 0
            for num in nums:
                ans += math.ceil(num / mid)
                if ans > threshold: return False
            return True    
        
        le, ri = 1, int(10**6)
        while le <= ri:
            mid = (le+ri) // 2
            if check(mid):
                ri = mid - 1
            else:
                le = mid + 1
        return le     