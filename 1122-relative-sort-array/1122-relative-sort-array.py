class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = collections.Counter(arr1)
        ans = []
        k = []
        for i in arr2:
            ans += [i] * dic[i]
            
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                k.append(arr1[i])
        k.sort()
        return ans + k