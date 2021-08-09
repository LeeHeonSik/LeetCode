class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x,y=0,0
        secret1 = list(secret)
        guess1 = list(guess)
        for i in range(len(secret1)):
            if secret1[i] == guess1[i]:
                x+=1
                secret1[i] = "A"
                guess1[i] = "B"
        for j in guess1:
            if j in secret1:
                y+=1
                secret1.remove(j)
        return ("%dA%dB" %(x,y))