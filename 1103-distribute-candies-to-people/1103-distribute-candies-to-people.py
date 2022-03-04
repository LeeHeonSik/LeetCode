class Solution:
    def distributeCandies(self, candies: int, n: int) -> List[int]:
        k = n*(n+1)//2
        ans = [0] * n
        c = 1
        while k <= candies:
            for i in range(n):
                ans[i] += c
                c += 1
            candies -= k
            k += n**2
            
        for i in range(n):
            if candies > c:
                ans[i] += c
                candies -= c
                c += 1
            else:
                ans[i] += candies
                break
        return ans