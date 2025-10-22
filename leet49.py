from collections import defaultdict
def groupAnagrams(strs):
        freq_maps = defaultdict(list)
        for s in strs:
            temp = [0] * 26
            for x in s:
                temp[ord(x) - ord("a")] += 1
            k = tuple(temp)
            freq_maps[k].append(s)
        return list(freq_maps.values())
