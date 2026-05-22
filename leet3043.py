class TrieNode:
    def __init__(self):
        self.children = [None]*10

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.offset = ord('0')

    def insert(self, num):
        node = self.root
        off = self.offset
        for c in str(num):
            c = ord(c)
            if not node.children[c-off]:
                node.children[c-off] = TrieNode()
            node = node.children[c-off]

    def match(self, num):
        node = self.root
        off = self.offset
        count = 0
        for c in str(num):
            c = ord(c)
            node = node.children[c-off]
            if not node: return count
            count += 1
        return count


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        a1 = set(arr1)
        a2 = set(arr2)

        if len(a1) < len(a2):
            a1, a2 = a2, a1

        t = Trie()

        for each in a1:
            t.insert(each)
            
        ans = 0

        for each in a2:
            x = t.match(each)
            if x > ans: ans = x
        
        return ans