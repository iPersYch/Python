def solution(n):
    roman_str = ''
    while n > 0:
        if n - 1000 >= 0:
            roman_str += "M"
            n = n - 1000
            continue
        elif n - 500 >= 0:
            roman_str += "D"
            n = n - 500
            continue
        elif n - 100 >= 0:
            roman_str += "C"
            n = n - 100
            continue
        elif n - 50 >= 0:
            roman_str += "L"
            n = n - 50
            continue
        elif n - 10 >= 0:
            roman_str += "X"
            n = n - 10
            continue
        elif n - 5 >= 0:
            roman_str += "V"
            n = n - 5
            continue
        elif n - 1 >= 0:
            roman_str += "I"
            n = n - 1
            continue
    roman_str = roman_str.replace("DCCCC", "CM")
    roman_str = roman_str.replace("CCCC", "CD")
    roman_str = roman_str.replace("LXXXX", "XC")
    roman_str = roman_str.replace("XXXX", "XL")
    roman_str = roman_str.replace("VIIII", "IX")
    roman_str = roman_str.replace("IIII", "IV")
    return roman_str


assert solution(1889) == 'MDCCCLXXXIX'
