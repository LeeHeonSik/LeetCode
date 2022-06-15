class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        prev = 0
        sp = "!@#$%^&*()-+"
        low, up, dig, spec = False, False, False, False
        if len(password) < 8:
            return False
        for i in password:
            if prev == i:
                return False
            if low == False:
                if i.islower():
                    low = True
            if up == False:
                if i.isupper():
                    up = True
            if dig == False:
                if i.isdigit():
                    dig = True
            if spec == False:
                if i in sp:
                    spec = True
            prev = i
        return low == up == dig == spec == True