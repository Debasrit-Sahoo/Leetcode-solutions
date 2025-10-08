def reverse(x):
        min_ = -2147483648 // 10
        max_ = 2147483647 // 10
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x != 0:
            temp = x % 10
            if rev > max_ or (rev == max_ and temp > 7):
                return 0
            rev = rev*10 + temp
            x = int(x / 10)
        return rev*sign
