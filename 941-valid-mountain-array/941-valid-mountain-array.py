def inc(idx, arr):
    for i in range(1, idx):
           if arr[i-1] >= arr[i]:
                return False
    return True

def dec(idx, arr):    
    for j in range(idx, len(arr)-1):
        if arr[j] <= arr[j+1]:
            return False
    return True

class Solution:  
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] > arr[1]:
            return False
        idx = 0
        for i in range(1, len(arr)):
            if arr[i-1] >= arr[i]:
                idx = i-1
                break
                
        left = inc(idx, arr)
        right = dec(idx, arr)
        
        return left == right == True