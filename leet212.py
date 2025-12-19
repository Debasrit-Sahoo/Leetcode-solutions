class Solution:
    class Trie:
        def __init__(self) -> None:
            self.map = defaultdict(lambda: Solution.Trie())
            self.word = False

        def insert(self, word: str) -> None:
            s = self
            for i in word:
                s = s.map[i]
            s.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board: return []
        t = self.Trie()
        for word in words:
            t.insert(word)
        r, c = len(board[0]), len(board)
        found = []
        def dfs(x: int, y: int, t: Solution.Trie) -> None:
            if not ((0 <= x < r) and (0 <= y < c)): return None
            char = board[y][x]
            if char == "%" or char not in t.map: return None
            board[y][x] = "%"
            v = t.map[char]
            if v.word: 
                found.append(v.word)
                v.word = False
            dfs(x+1, y, v)
            dfs(x-1, y, v)
            dfs(x, y+1, v)
            dfs(x, y-1, v)
            board[y][x] = char
            if not v.word and not v.map: del t.map[char]
        for i in range(r):
            for j in range(c):
                dfs(i, j, t)

        return found