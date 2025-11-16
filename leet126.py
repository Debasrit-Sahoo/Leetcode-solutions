from collections import deque,defaultdict
def findLadders(beginWord, endWord, wordList):
        if beginWord not in wordList:
            wordList.append(beginWord)
        graph = defaultdict(list)
        le = len(beginWord)
        for word in wordList:
            for i in range(le):
                p = word[:i] + "*" + word[i+1:]
                graph[p].append(word)
        parents = defaultdict(list)
        stack = deque([beginWord])
        seen = set([beginWord])

        while stack:
            l = len(stack)
            local_seen = set([])
            for _ in range(l):
                cur = stack.popleft()
                for i in range(le):
                    p = cur[:i] + "*" + cur[i+1:]
                    for word in graph[p]:
                        if word in seen:
                            continue
                        parents[word].append(cur)
                        if word not in local_seen:
                            stack.append(word)
                            local_seen.add(word)
            seen.update(local_seen)
            if endWord in local_seen:
                break

        out = []
        def constructor(key, l):
            if key == beginWord:
                out.append(l[::-1] + [endWord])
            else:
                for x in parents[key]:
                    l.append(x)
                    constructor(x, l)
                    l.pop()
        constructor(endWord, [])
        return out