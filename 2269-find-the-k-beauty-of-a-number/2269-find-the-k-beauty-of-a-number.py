class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        s = str(num)
        n = len(s)
        for i in range(0,n-k+1):
            try:
                if num % int(s[i:i+k]) == 0:
                    ans += 1
            except:
                continue
        return ans