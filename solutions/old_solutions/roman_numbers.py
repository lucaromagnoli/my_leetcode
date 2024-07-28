class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        roman = list(s)
        values = []
        i = 0
        while i < len(roman):
            if i + 1 < len(roman):
                if roman[i] == "I" and roman[i + 1] in ("V", "X"):
                    values.append(symbols[roman[i + 1]] - 1)
                    i += 2
                elif roman[i] == "X" and roman[i + 1] in ("L", "C"):
                    values.append(symbols[roman[i + 1]] - 10)
                    i += 2
                elif roman[i] == "C" and roman[i + 1] in ("D", "M"):
                    values.append(symbols[roman[i + 1]] - 100)
                    i += 2
                else:
                    values.append(symbols[roman[i]])
                    i += 1
            else:
                values.append(symbols[roman[i]])
                i += 1
        return sum(values)

    def intToRoman(self, int_num: int) -> str:
        symbols_map = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        digits = str(int_num)
        romans = []
        column = 10 ** (len(digits) - 1)
        for d in digits:
            mul = int(d)
            if mul <= 5 or mul == 9:
                if mul <= 3:
                    romans.append(symbols_map[column] * mul)
                else:
                    num = mul * column
                    romans.append(symbols_map[num])
            elif 5 < mul < 9:
                romans.append(symbols_map[5 * column])
                mul = (mul * column) - (5 * column)
                mul = int(mul / column)
                romans.append(symbols_map[column] * mul)
            column = int(column / 10)
        return "".join(romans)


if __name__ == "__main__":
    solution = Solution()
    r = solution.intToRoman(3749)
    print(r)
