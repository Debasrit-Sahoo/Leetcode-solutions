from collections import defaultdict
class WordDictionary:

    def __init__(self):
        self.map = defaultdict(WordDictionary)
        self.isword = False

    def addWord(self, word: str) -> None:
        p = self
        for i in word:
            p = p.map[i]
        p.isword = True
        
    def search(self, word: str, mem= None) -> bool:
        if not mem:
            mem = {}
        key = (id(self), word)
        if key in mem:
            return mem[key]
        if not word:
            mem[key] = self.isword
            return self.isword
        
        c = word[0]
        if c == ".":
            for v in self.map.values():
                if v.search(word[1:],mem):
                    mem[key] = True
                    return True
            mem[key] = False
        else:
            if c not in self.map: mem[key] = False
            else: mem[key] = self.map[c].search(word[1:],mem)
        return mem[key]