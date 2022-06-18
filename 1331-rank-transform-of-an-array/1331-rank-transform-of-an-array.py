class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))
        d = {}
        ans = []
        for i in range(len(temp)):
            d[temp[i]] = i+1
        for i in range(len(arr)):
            ans.append(d[arr[i]])
        return ans