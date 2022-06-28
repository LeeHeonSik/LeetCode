class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        al = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        temp = []
        for w in words:
            k = ''
            for s in w:
                k += al[ord(s) - 97]
            if k not in temp:
                temp.append(k)
        return len(temp)