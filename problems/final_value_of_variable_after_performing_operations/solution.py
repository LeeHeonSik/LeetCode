class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dic = {"++X" : 1, "X++" : 1, "--X" : -1, "X--" : -1}
        ans = 0
        for i in operations:
            ans += dic[i]
        return ans