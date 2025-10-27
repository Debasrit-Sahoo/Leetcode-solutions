def isNumber(s):
        s = s.strip()
        dec, dig, exp = 0, 0, 0
        for i, char in enumerate(s):
            if char.isdigit():
                dig = 1
            elif char == ".":
                if dec or exp:
                    return False
                dec = 1
            elif char == "+" or char == "-":
                if i != 0 and s[i-1].lower() != "e":
                    return False
            elif char.lower() == "e":
                if exp or not dig:
                    return False
                dig = 0
                exp = 1
            else:
                return False
        return bool(dig)
