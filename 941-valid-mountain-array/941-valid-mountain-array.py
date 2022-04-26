class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = arr.index(max(arr))
        if n == 0 or n == len(arr)-1:
            return False
        for i in range(1,n):
            if arr[i-1] >= arr[i]:
                return False
        for j in range(n+1,len(arr)):
            if arr[j-1] <= arr[j]:
                return False
        return True