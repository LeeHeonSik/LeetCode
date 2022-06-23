class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        se = sentence.split()
        for i in range(len(se)):
            if searchWord == se[i][:len(searchWord)]:
                return i+1
        return -1