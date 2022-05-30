class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(2,num+1):
            k = i
            s = 0
            while k != 0:
                s += k%10
                k //= 10
            if s % 2 == 0:
                ans += 1
        return ans