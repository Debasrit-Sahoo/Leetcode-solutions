class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        arr = [0]*26
        for c in word:
            x = ord(c)

            if x < 91:
                arr[x - 65] |= 2
            else:
                arr[x - 97] |= (4 if arr[x - 97] & 2 else 1)

        return sum(a == 3 for a in arr)