class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in arr:
            if i*2 in arr:
                if i != 0:
                    return True
                else:
                    if arr.count(0) >= 2:
                        return True
        return False