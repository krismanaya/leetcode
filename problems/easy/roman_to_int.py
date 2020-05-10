roman_s = {
                "IV": 4,
                "IX": 9,
                "XL": 40,
                "XC": 90,
                "CD": 400,
                "CM": 900
        }

roman = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
            }

def romanToInt(s: str) -> int:
    sum = 0
    while s:
        r = s[0] + s[1]
        if r in roman_s.keys():
            sum += roman_s[r]
            s = s[2: len(s)]
            if len(s) == 1:
                sum += roman[s[0]]
                break
        else:
            sum += roman[s[0]]
            s = s[1: len(s)]
            if len(s) == 1:
                sum += roman[s[0]]
                break