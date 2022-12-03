### Честно говоря, это один из самых тупых способов решения
def romanToInt(s):
    s_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    counter = 0
    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")
    print(s)
    for i in s:
        if i in s_dict:
            counter += s_dict[i]
    return counter




assert romanToInt('MCMXCIV')==1994