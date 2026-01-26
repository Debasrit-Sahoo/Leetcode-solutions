class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        stack = []
        scale = ["", "Thousand", "Million", "Billion"]
        w20s = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen" ,"Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        w10s = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        while num > 0:
            stack.append(num%1000)
            num //= 1000
        res = []
        c = len(stack) - 1
        tl = []
        while stack:
            n = stack.pop()
            if n == 0: c -= 1; continue
            if n >= 100:
                tl.append(w20s[n // 100] + " Hundred")
                n %= 100
            if n >= 20:
                tl.append(w10s[n // 10])
                n %= 10
            if n > 0:
                tl.append(w20s[n])
            if scale[c]: tl.append(scale[c])
            res.append(" ".join(tl))
            tl.clear()
            c -= 1
        return " ".join(res)