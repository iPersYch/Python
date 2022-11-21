# Itertools for sure will be there :)
import itertools
import random
import math

word = 'сонгри'  #
word_length = 3


def word_to_words_v1(a=word, b=word_length):
    comb = itertools.permutations(a, b)
    array = [''.join(i) for i in comb]
    return print(sorted(array), '-----------  Способ через итертул')


# Random ragemode will be there:)
array_with_newWords_notSplited = []


def word_to_words_v2(a=word, b=word_length):  # Функция создает слово по заданным параметрам
    str_array = ''
    empty_array = []
    array_with_newwords = []
    for i in a:
        empty_array.append(i)
    while len(empty_array) > (len(a) - b):
        random_digit = random.randint(0, len(empty_array) - 1)
        array_with_newwords.append(empty_array[random_digit])
        empty_array.pop(random_digit)
        str_array = ''.join(array_with_newwords)
    return str_array


def word_in_list(a=word, b=word_length):  # Функция вызывает предыдующую, которое создает слово, и проверяет есть ли оно в моем списке
    while len(set(array_with_newWords_notSplited)) < math.factorial(len(a)) / math.factorial(
            len(a) - b):
        clean = word_to_words_v2(a, b)  # Вызываю функцию, которая генерирует слово
        if clean in array_with_newWords_notSplited:  # Проверяю есть ли ужеслово в списке. Время 4 часа утра, почему то проверка на вхождение срабатывала, но все равно появлялись дубликаты, пришлось делать множество, чтобы избавиться от них
            continue
        else:
            array_with_newWords_notSplited.append(word_to_words_v2(a, b))
    return print(sorted(list(set(array_with_newWords_notSplited))), '-----------  Способ через рандом')


word_to_words_v1()  # Хоть способ через не особо продуктивный, но закончить его было делом принципа. Тут костыль в костыле просто :) И на больших числах он думает ооооочень долго.
word_in_list()


