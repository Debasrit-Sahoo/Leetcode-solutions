def mf(num):
        dic = { 
            1000 : "M",
            100 : "C",
            10 : "X",
            1 : "I",
            500 : "D",
            50 : "L",
            5 : "V"
        }
        temp = ""
        i = 1000
        while num > 0:
            if num >= i:
                c = num // i
                if c == 9:
                    temp = temp + dic[i] + dic[i*10]
                    num -= i*c
                elif c >= 5:
                    temp = temp + dic[i*5]
                    num -= i*5
                    t = num // i
                    temp = temp + dic[i]*t
                    num -= i*t
                if c == 4:
                    temp = temp + dic[i] + dic[i*5]
                    num -= i*c
                if c < 4:
                    temp = temp + dic[i]*c
                    num -= i*c
            i = i // 10
        return temp
