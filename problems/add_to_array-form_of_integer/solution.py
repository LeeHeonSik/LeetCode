class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = ''.join(map(str, num))
        s = int(s) + k
        return list(str(s))