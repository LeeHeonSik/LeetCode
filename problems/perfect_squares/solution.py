class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i **2 for i in range(1, int(n**(1/2)) + 1)]
        nums = {n}
        result = 0
        while 0 not in nums:
            nums = {num - square for num in nums for square in squares if num - square >= 0}
            result += 1
        return result