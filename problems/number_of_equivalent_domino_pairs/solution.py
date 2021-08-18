class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        count = Counter()

        for i in dominoes:
            key = min(i[0], i[1]) * 10 + max(i[0], i[1])
            ans += count[key]
            print(count[key])
            count[key] += 1

        return ans