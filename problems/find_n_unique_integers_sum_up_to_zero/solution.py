class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 1:
            ans = [0]
        else:
            ans = []
        for i in range(1, n//2 + 1):
            ans.append(i)
            ans.append(-i)
        return ans