class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = Counter(arr)
        for i, j in dic.items():
            if j == 1:
                k -= 1
                if k == 0:
                    return i
        return ""