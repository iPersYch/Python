"""
In this Kata you have to create a function,named insertMissingLetters,that takes in a string and outputs the same string processed in a particular way.

The function should insert only after the first occurrence of each character of the input string, all the alphabet letters that:

-are NOT in the original string
-come after the letter of the string you are processing

Each added letter should be in uppercase, the letters of the original string will always be in lowercase.
"""

def insert_missing_letters(st:str)->str:
    new_word=''
    missing_letters=''
    missing_letters+= ''.join(x for x in "abcdefghijklmnopqrstuvwxyz" if x not in st)
    if len(st)==0 or st=='abcdefghijklmnopqrstuvwxyz':
        return 'abcdefghijklmnopqrstuvwxyz'
    for i in st:
        for j in missing_letters:
            if i=='z':
                new_word+='z'
                break
            if i in new_word:
                new_word+=i
                break
            if j>=i:
                new_word+=i+''.join(x for x in missing_letters[missing_letters.find(j)::].upper())
                break
            if i>max(missing_letters):
                new_word+=i
                break
    return new_word


insert_missing_letters('tqjkawerjwftgzybucxzikpeweqvoxiufunbqva')

# qSjLMSkLMSaDHLMSeHLMSrSjfHLMSgHLMSzbDHLMScDHLMSziLMSkpSeeqoSifnSbqa
# tqSjLMSkLMSaDHLMSweHLMSrSjwfHLMStgHLMSzybDHLMSucDHLMSxziLMSkpSeweqvoSxiufunSbqva

