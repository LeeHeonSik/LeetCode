class Solution:
    def reorderSpaces(self, text: str) -> str:
        d = {' ': 0}
        for i in text:
            if i == ' ':
                d[i] += 1
        text = text.split()
        
        if len(text) == 1:
            return text[0]+(' ' * d[' '])
        l, x = d[' '] // (len(text) - 1), d[' '] % (len(text) - 1)
        return (' '*l).join(text) + (' '*x)