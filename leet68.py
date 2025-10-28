def fullJustify(words, maxWidth):
        out = []
        cur = []
        pointer, line_len = 0, 0
        while pointer < len(words):
            word = words[pointer]
            if line_len + len(word) <= maxWidth:
                if line_len+len(word)+1<= maxWidth:
                    cur.append(word + " ")
                    line_len += len(word)+1
                    pointer += 1
                else:
                    cur.append(word)
                    line_len += len(word)
                    pointer += 1
            else:
                print(cur)
                gap = len(cur)
                if cur[-1] == cur[-1].strip() and gap > 1:
                    out.append("".join(cur))
                    cur.clear()
                    line_len = 0
                else:
                    if cur[-1] != cur[-1].strip():
                        cur[-1] = cur[-1].strip()
                        line_len -= 1
                    if gap <= 1:
                        out.append(cur[0] + " "*(maxWidth-line_len))
                        cur.clear()
                        line_len = 0
                    else:
                        gap -= 1
                        padding = (maxWidth - line_len) // gap
                        extra = (maxWidth - line_len) % gap
                        print(gap, line_len, padding, extra)
                        for x in range(extra):
                            cur[x] = cur[x] + " "
                        out.append((" "*padding).join(cur))
                        cur.clear()
                        line_len = 0
        if cur:
            cur[-1] = cur[-1].strip()
            s = "".join(cur)
            if len(s) < maxWidth:
                s = s + (maxWidth - len(s))*" " 
            out.append(s)
        return out