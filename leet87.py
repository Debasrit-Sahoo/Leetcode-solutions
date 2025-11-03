from collections import Counter
from functools import lru_cache
def isScramble(s1, s2):
        @lru_cache(None)
        def hellspawn_unscrambler(il, ir, ol,or_):
            if ir - il <= 1:
                return True if s1[il]==s2[ol] else False
            if Counter(s1[il:ir]) != Counter(s2[ol:or_]):
                return False
            else:
                for i in range(il + 1, ir):
                    not_rev = hellspawn_unscrambler(il, i, ol, ol + (i - il)) and hellspawn_unscrambler(i, ir, ol + (i - il), or_)
                    rev = hellspawn_unscrambler(il, i, or_ - (i - il), or_) and hellspawn_unscrambler(i, ir, ol, or_ - (i - il))
                    if not_rev or rev:
                        return True
                return False
        return hellspawn_unscrambler(0, len(s1), 0, len(s2))