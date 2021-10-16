class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        t = releaseTimes[0]
        ans = keysPressed[0]
        for i in range(1,len(releaseTimes)):
            if t < releaseTimes[i] - releaseTimes[i-1]:
                t = releaseTimes[i] - releaseTimes[i-1]
                ans = keysPressed[i]
            elif t == releaseTimes[i] - releaseTimes[i-1]:
                ans = chr(max(ord(ans), ord(keysPressed[i])))
        return ans