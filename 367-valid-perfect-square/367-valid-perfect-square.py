class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        st = 0
        end = 2**31 - 1
        
        while st <= end:
            n = (st + end) // 2
            m = n**2
            if m > num:
                end = n-1
            elif m < num:
                st = n+1
            else:
                return True
        return False
            