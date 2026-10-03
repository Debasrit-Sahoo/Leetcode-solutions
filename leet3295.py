class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned = set(bannedWords)
        c = 0
        for each in message:
            if each in banned:
                c += 1
                if c == 2: 
                    return True
        else:
            return False