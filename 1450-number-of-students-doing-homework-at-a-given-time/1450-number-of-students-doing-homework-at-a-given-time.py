class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for s in range(len(startTime)):
            if startTime[s]<= queryTime <= endTime[s]:
                ans += 1
        return ans