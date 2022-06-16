class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        while i < len(words):
            if sorted(list(words[i])) == sorted(list(words[i-1])):
                words.pop(i)
            else:
                i += 1
        return words