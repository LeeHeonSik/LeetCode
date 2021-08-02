class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulo = (10**9 + 7)
        even = ((n + 1) // 2)
        odd = (n // 2)
        ans1=pow(5,even,modulo)
        ans2=pow(4,odd,modulo)
        return (ans1 * ans2) % modulo