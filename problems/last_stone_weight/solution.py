class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 3:
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            if x == y:
                continue
            elif x != y :
                stones.append(y-x)
                
        if len(stones) == 1:
            return stones[0]
        else:
            return abs(stones[1] - stones[0])