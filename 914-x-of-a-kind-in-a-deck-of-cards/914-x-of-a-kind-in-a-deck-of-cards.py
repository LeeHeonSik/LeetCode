class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic = collections.Counter(deck)
        return math.gcd(*dic.values()) >= 2