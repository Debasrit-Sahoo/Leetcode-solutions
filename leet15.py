def threeSum(num):
        num.sort()
        f = []
        for i in range(len(num)):
            j, k = i + 1, len(num) - 1
            v = 0 - num[i]
            if i > 0 and num[i] == num[i - 1]:
                continue
            while j < k:
                x = num[j] + num[k]
                if v == x:
                    f.append([num[i], num[j], num[k]])
                    j += 1
                    while j < k and num[j] == num[j-1]:
                        j += 1
                    k -= 1
                    while j < k and num[k] == num[k+1]:
                        k -= 1
                elif x < v:
                    j += 1
                    while j < k and num[j] == num[j-1]:
                        j += 1 
                else:
                    k -= 1
                    while j < k and num[k] == num[k+1]:
                        k -= 1
        return f