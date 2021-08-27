class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        h = 0
        for i in gain:
            ans += i
            if ans > h :
                h = ans
        return h