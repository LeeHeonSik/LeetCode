class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if x == 0:
            return 0
        if min(nums) > x:
            return -1
        t = sum(nums) - x
        if t == 0:
            return len(nums)
        if t < 0:
            return -1
        
        s = 0
        m = 0
        S = 0
        for i in range(len(nums)):
            S += nums[i]
            if S > t:
                while S > t:
                    S -= nums[s]
                    s += 1
            if S == t:
                m = max(m, i - s + 1)
        return len(nums) - m