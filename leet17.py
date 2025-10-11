def letterCombinations(digits):
        vals = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        lst = [""]
        for i in digits:
                val = vals[i]
                temp_lst = []
                for j in lst:
                        for k in val:
                                temp_lst.append(j + k)
                lst = temp_lst
        return lst