class Solution:
    def countPoints(self, rings: str) -> int:
        ans = 0
        k = [{'B' :0, 'R' : 0, 'G' : 0},{'B' :0, 'R' : 0, 'G' : 0},{'B' :0, 'R' : 0, 'G' : 0},{'B' :0, 'R' : 0, 'G' : 0},{'B' :0, 'R' : 0, 'G' : 0},{'B' :0, 'R' : 0, 'G' : 0},{'B' :0, 'R' : 0, 'G' : 0},{'B' :0, 'R' : 0, 'G' : 0},{'B' :0, 'R' : 0, 'G' : 0},{'B' :0, 'R' : 0, 'G' : 0}]
        for i in range(0, len(rings), 2):
            k[int(rings[i+1])][rings[i]] += 1
        
        for kk in k:
            if all(i >= 1 for i in kk.values()):
                ans += 1
        return ans