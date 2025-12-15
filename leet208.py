from collections import defaultdict
class Trie:

    def __init__(self):
        self.root = defaultdict(Trie)
        self.is_word = False

    def insert(self, word: str) -> None:
        p = self
        for i in word:
            p = p.root[i]
        p.is_word = True

    def search(self, word: str) -> bool:
        p = self
        for i in word:
            if i not in p.root:
                return False
            p = p.root[i]
        return p.is_word

    def startsWith(self, prefix: str) -> bool:
        p = self
        for i in prefix:
            if i not in p.root:
                return False
            p = p.root[i]
        return True