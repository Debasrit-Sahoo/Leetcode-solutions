def multiply(num1, num2):
        num1 = [int(x) for x in num1]
        num2 = [int(y) for y in num2]
        num1 = num1[::-1]
        num2 = num2[::-1]
        lst = []
        c1 = 1
        result = 0
        for i in num1:
            c = 1
            temp = 0
            for j in num2:
                temp += i * j * c
                c = c * 10
            result = result + temp * c1
            c1 = c1 * 10
        return str(result)