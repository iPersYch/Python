def pig_it(text):
    splitted_text= text.split()
    pig=''
    print(splitted_text)
    for i in splitted_text:
        if not i.isalpha():
            pig+=i
        else:
            pig+=i[1:len(i)]+i[0]+'ay '
    return print(pig)


# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])














pig_it('Pig latin is cool')




