def findSubstring(s, words): 
        d = {}
        for i in words:
            d[i] = d.get(i, 0) + 1
        chunk_len = len(words[0])
        window = len(words) * chunk_len
        i = 0
        out = []
        while i+window <= len(s):
            x = 0
            seen = {}
            while x < window:
                chunk = s[i+x:i+x+chunk_len]
                seen[chunk] = seen.get(chunk, 0) + 1
                x += chunk_len 
            if d == seen:
                out.append(i)
            i += 1
        return out