class Solution:
    def wordPattern(self, pattern: str, s) -> bool:
        s = s.split()
        if len(pattern) != len(s): return False
        used_vals = set()
        seen = {}
        for i in range(len(pattern)):
            if pattern[i] in seen:
                if seen[pattern[i]] != s[i]:return False
            elif s[i] in used_vals: return False
            else: seen[pattern[i]] = s[i]; used_vals.add(s[i])
        return True