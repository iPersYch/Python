# Itertools for sure will be there :)
import itertools
import random
import math
import time

word = 'ABCDE'
word_length = 2


def word_to_words_v1(a=word, b=word_length):
    start =time.time()
    comb = itertools.permutations(a, b)
    array = [''.join(i) for i in comb]
    end = time.time()-start
    return sorted(array)


# Random ragemode will be there:)






def word_in_list(a=word, b=word_length):  # Функция вызывает предыдующую, которое создает слово, и проверяет есть ли оно в моем списке
    array_with_newWords_notSplited = []
    def word_to_words_v2():  # Функция создает слово по заданным параметрам
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
    start = time.time()
    while len(set(array_with_newWords_notSplited)) < math.factorial(len(a)) / math.factorial(
            len(a) - b):
        clean = word_to_words_v2()  # Вызываю функцию, которая генерирует слово
        if clean in array_with_newWords_notSplited:  # Проверяю есть ли ужеслово в списке. Время 4 часа утра, почему то проверка на вхождение срабатывала, но все равно появлялись дубликаты, пришлось делать множество, чтобы избавиться от них
            continue
        else:
            array_with_newWords_notSplited.append(word_to_words_v2())
    end = time.time()-start
    return sorted(list(set(array_with_newWords_notSplited)))


# Так же способ расчитанный на рандом, но сделанный через срезы и шафл

def shuffled_arr(a=word,b=word_length): #Провел гениальный рефакторинг,засунув функцию в функцию, что позволило нормально прогонять автотесты
    def shuffle_words():
        charlst = list(a)
        random.shuffle(charlst)
        new_word = ''.join(charlst)
        return new_word[:b]
    start=time.time()
    shuf_list=[]
    while len(shuf_list) < math.factorial(len(a)) / math.factorial(len(a) - b):
        shuffle_word = shuffle_words()
        if shuffle_word not in shuf_list:
            shuf_list.append(shuffle_word)
        else:
            continue
    end=time.time()-start
    return sorted(shuf_list)

word_to_words_v1()
word_in_list() # Хоть способ через не особо продуктивный, но закончить его было делом принципа. Тут костыль в костыле просто :) И на больших числах он думает ооооочень долго.
shuffled_arr() # Способ похож, на предыдущий, но выполнен иначе, благодаря чему скорость выполнения выше в несколько раз

# На данном этапе я пришел к выводу, что с длинными словами будет работать только итертул.
# Хоть мне и удалось оптимизировать код, через шафл и он начал работать быстрее этого недостаточно.
# Необходимо придумать алгоритм, который исключит лишнии комбинации, которые появляются при рандоме и шафле.
# AHTUNG! Понял, что данный вариант не будет работать если в слове есть одинаковые буквы. Придумать, как решить