class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right + 1):
            c = str(i)
            if all((int(k) != 0 and i % int(k) == 0) for k in c):
                ans.append(i)
        return ans