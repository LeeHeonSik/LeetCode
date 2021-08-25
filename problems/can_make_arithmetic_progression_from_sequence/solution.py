class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        a = arr[0]
        n = len(arr)
        if sum(arr) == n*(2*a + (n-1)*diff)/2 :
            for i in range(1,n):
                if arr[i] - arr[i-1] != diff:
                    return False
            return True
        return False