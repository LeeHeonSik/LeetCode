class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ray = matrix[0]
        
        for i in range(1,len(matrix)):
            for j in matrix[i]:
                ray.append(j)
        
        return sorted(ray)[k-1]