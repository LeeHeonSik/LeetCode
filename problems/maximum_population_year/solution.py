class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        _min = min(map(min,logs))
        _max = max(map(min,logs))
        year = 0
        pop = 0
        for i in range(_min,_max+1):
            cnt = 0
            for j in range(len(logs)):
                if logs[j][0] <= i < logs[j][1] :
                    cnt+=1
            if cnt > pop :
                pop = cnt
                year = i
        return year