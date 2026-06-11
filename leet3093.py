class Solution:
    class TrieNode:
        __slots__ = ("children", "best_len", "best_idx")
        def __init__(self):
            self.children = [None]*26
            self.best_len = 1 << 31
            self.best_idx = 1 << 31

    class Trie:
        def __init__(self):
            self.root = Solution.TrieNode()
            self.offset = ord('a')

        def insert(self, word, idx):
            n = len(word)
            node = self.root
            off = self.offset
            for c in word:
                i = ord(c) - off

                if (n < node.best_len or (n == node.best_len and idx < node.best_idx)):
                    node.best_len = n
                    node.best_idx = idx

                if not node.children[i]:
                    node.children[i] = Solution.TrieNode()
                
                node = node.children[i]
            if (n < node.best_len or (n == node.best_len and idx < node.best_idx)):
                node.best_len = n
                node.best_idx = idx

        def search(self, word):
            node = self.root
            off = self.offset
            for c in word:
                i = ord(c) - off
                nxt = node.children[i]
                if not nxt: break
                node = nxt

            return node.best_idx


    def stringIndices(self, words: List[str], queries: List[str]) -> List[int]:
        trie = self.Trie()
        for idx, each in enumerate(words):
            trie.insert(each[::-1], idx)

        for idx, each in enumerate(queries):
            queries[idx] = trie.search(each[::-1])

        return queries

        