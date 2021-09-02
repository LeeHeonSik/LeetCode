class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        L = len(arr)
        for i in range(L):
            for k in range(i+1,L):
                if abs(arr[i] - arr[k]) <= c:
                    for j in range(i+1,k):
                        if abs(arr[j] - arr[k]) <=b and abs(arr[i] - arr[j]) <= a :
                            ans+=1
        return ans