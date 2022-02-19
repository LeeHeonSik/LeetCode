class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic = {}
        for i in pieces:
            dic[i[0]] = i
        t, len_arr = 0, len(arr)
        while t < len_arr:
            if (arr[t] in dic and
                    arr[t: t + len(dic[arr[t]])] == dic[arr[t]]):
                t += len(dic[arr[t]])
            else:
                return False
        return True