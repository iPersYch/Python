def wave(people: str):
    fin_arr=[]
    for i in range(len(people)):
        if people[i] !=" ":
            if i==0:
                fin_arr.append(people.lower().capitalize())
            else:
                word=people.lower()[:i]+people.lower()[i].upper()+people[i+1:].lower()
                fin_arr.append(word)
    return print(fin_arr)

wave("ABCDEFGHIJKLMNOPQR")