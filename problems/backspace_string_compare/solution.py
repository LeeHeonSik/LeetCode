class Solution(object):
    def backspaceCompare(self, s, t):
            ans1 = []
            ans2 = []
            for c in s:
                if c != '#':
                    ans1.append(c)
                elif ans1:
                    ans1.pop()
            for c in t:
                if c != '#':
                    ans2.append(c)
                elif ans2:
                    ans2.pop()
            return ans1 == ans2