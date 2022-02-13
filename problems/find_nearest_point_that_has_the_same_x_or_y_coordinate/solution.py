class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        t = 2*10**4
        for i in range(len(points)):
            a, b = points[i][0], points[i][1]
            if a == x or b == y:
                k = (abs(a-x) + abs(b-y))
                if k < t:
                    t = k
                    ans = i
        return ans