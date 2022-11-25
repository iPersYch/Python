def addTwoNumbers(l1: list, l2):
    str_l1 = ''
    str_l2 = ''
    l1.reverse()
    l2.reverse()
    for i in l1:
        str_l1 += ''.join(str(i))
    for i in l2:
        str_l2 += ''.join(str(i))
    return print(int(str_l1) + int(str_l2))


addTwoNumbers([2, 4, 3], [5, 6, 4])
