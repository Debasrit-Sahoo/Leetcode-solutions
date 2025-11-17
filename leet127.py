from collections import deque,defaultdict
def ladderLength(beginWord, endWord, wordList):
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return 0
        l_ = len(beginWord)
        graph = defaultdict(list)
        for word in wordList:
            for i in range(l_):
                p = word[:i] + "*" + word[i+1:]
                graph[p].append(word)
        queue = deque([beginWord])
        used = set([beginWord])
        d = 0
        while queue:
            l = len(queue)
            loc_used = set([])
            d += 1
            for _ in range(l):
                cur = queue.popleft()
                for i in range(l_):
                    p = cur[:i] + "*"+ cur[i+1:]
                    for word in graph[p]:
                        if word in used:
                            continue
                        if word not in loc_used:
                            queue.append(word)
                            loc_used.add(word)
            if endWord in used:
                return d
            used.update(loc_used)
        return 0