""" Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
 that occur more than once in the input string. The input string can be assumed to contain only alphabets (both
uppercase and lowercase) and numeric digits. """


def duplicate_count(text: str) -> int:
    counter = 0
    chars_dic = dict.fromkeys([x for x in [i for i in text.lower()]], 0)
    for i in chars_dic.keys():
        for j in [x for x in text.lower()]:
            if i == j:
                chars_dic[i] += 1
    for i in chars_dic.keys():
        if chars_dic[i] > 1:
            counter += 1
    return counter


if __name__ == '__main__':
    assert duplicate_count("Indivisibilities") == 2
    assert duplicate_count("ABCabc") == 3
    assert duplicate_count("") == 0
    assert duplicate_count("1234567890") == 0


