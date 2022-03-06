class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        dic = collections.Counter(candyType)
        n = len(candyType) // 2
        if len(dic.keys()) >= n:
            return n
        else:
            return len(dic.keys())