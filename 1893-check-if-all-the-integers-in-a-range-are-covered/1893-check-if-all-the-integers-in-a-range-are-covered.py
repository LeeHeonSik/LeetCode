class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            if all(not(j[0] <= i <= j[1]) for j in ranges):
                    return False
        return True