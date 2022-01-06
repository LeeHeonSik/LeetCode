
from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        dic = {}
        for i in range(1, len(tiles)+1):
            t = permutations(tiles, i)
            for x in t:
                dic[x] = dic.get(x, 0) + 1
        return len(dic)