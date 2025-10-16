from collections import deque
def findSubstring(s, words): 
    freq_map = {}
    for w in words:
        freq_map[w] = freq_map.get(w, 0) + 1
    chunk_length = len(words[0])
    window_length = len(words) * chunk_length
    window = deque()
    output = []
    for i in range(chunk_length):
        window_end = i + window_length
        window = deque()
        while i + chunk_length <= window_end:
            window.append(s[i:i+chunk_length])
            i += chunk_length
        seen = {}
        for c in window:
            seen[c] = seen.get(c, 0) + 1
        
        while i <= len(s):
            if seen == freq_map:
                output.append(i - window_length)

            leaving = window.popleft()
            seen[leaving] -= 1
            if seen[leaving] == 0:
                del seen[leaving]

            arriving = s[i:i + chunk_length]
            window.append(arriving)
            seen[arriving] = seen.get(arriving, 0) + 1

            i += chunk_length
    return output