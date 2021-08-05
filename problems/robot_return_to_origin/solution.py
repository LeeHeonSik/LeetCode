class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dic={'U' : 0, 'D' : 0, 'R' : 0, 'L' : 0}
        for i in moves:
            dic[i]=dic.get(i,0)+1
        if dic['U'] != dic['D'] or dic['L'] != dic['R']:
            return False
        return True