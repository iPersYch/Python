import pytest
import string
import random
from Word_to_Words import shuffled_arr,word_to_words_v1, word_in_list

#Тут создам рандомные входные значения строки и длины
all_chars= list(string.ascii_lowercase)
random.shuffle(all_chars)
random_digit=random.randint(1,6)
random_word=''.join(all_chars)[:random_digit]

# Тут получаем результат итртула, с рандомными строками и длинной
ittertool_result=word_to_words_v1(random_word,random_digit)
# Проверяем способ через шафл, равны ли значения с итертулом, пришлось изменить структура функции шафл, чтобы прогонялись автотесты
def test_shuffled_arr():
    shuffled_arr_result=shuffled_arr(random_word,random_digit)
    print(ittertool_result,)
    print(shuffled_arr_result)
    assert ittertool_result==shuffled_arr_result

def test_word_in_list():
    word_in_list_result=word_in_list(random_word,random_digit)
    assert word_in_list_result==ittertool_result


