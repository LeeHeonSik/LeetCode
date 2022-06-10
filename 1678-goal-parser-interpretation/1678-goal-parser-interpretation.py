class Solution:
    def interpret(self, command: str) -> str:
        prev = False
        ans = ''
        for i in range(len(command)):
            k = command[i]
            if prev:
                if k == ')':
                    ans += 'o'
                else:
                    ans += k
                prev = False
            elif k == '(':
                prev = True
            elif k != ')':
                ans += k
        return ans