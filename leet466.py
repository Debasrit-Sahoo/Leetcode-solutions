class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        sn2 = len(s2)

        bc = [None]*sn2
        mc = [None]*sn2

        block_count = match_count = j_ptr_idx = 0
        a, b = s1, s2
        while (bc[j_ptr_idx] == None):
            
            bc[j_ptr_idx], mc[j_ptr_idx] = block_count, match_count

            for c in a:
                if (c == b[j_ptr_idx]):
                    j_ptr_idx+=1
                    if j_ptr_idx == sn2:
                        j_ptr_idx = 0
                        match_count += 1

            block_count += 1

        blocks = block_count - bc[j_ptr_idx]
        matches = match_count - mc[j_ptr_idx]

        rem_blocks = n1 - block_count
        cycles = rem_blocks // blocks
        match_count += cycles * matches
        block_count += cycles * blocks

        for _ in range(n1 - block_count):
            for c in s1:
                if c == s2[j_ptr_idx]:
                    j_ptr_idx += 1
                    if j_ptr_idx == sn2:
                        j_ptr_idx = 0
                        match_count += 1
                
        return match_count // n2
