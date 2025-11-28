class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        i = 0
        while i < len(v1) or i < len(v2):
            a = int(v1[i]) if i < len(v1) else 0
            b = int(v2[i]) if i < len(v2) else 0
            if a > b:
                return 1
            if a < b:
                return -1
            i += 1
        return 0 