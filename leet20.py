def isValid(s):
    if len(s) % 2 != 0:
        return False
    stack = []
    sym = {
        "(":")",
        "{":"}",
        "[":"]"
    }
    for i in s:
        if i in sym:
            stack.append(sym[i])
            continue
        if not stack or i != stack.pop():
            return False
    return not stack
