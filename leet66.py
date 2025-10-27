def plusOne(digits):
        x = -1
        c = 1
        while -x <= len(digits):
            temp = digits[x] + c
            if temp >= 10:
                temp -= 10
                digits[x] = temp
                x -= 1
            else:
                digits[x] = temp
                c = 0
                break
        if c:
            digits.insert(0,1)
        return digits