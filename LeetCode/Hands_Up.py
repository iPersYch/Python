"""Imagine that you have an array of 3 integers each representing a different person. Each number can be 0, 1,
or 2 which represents the number of hands that person holds up.

Now imagine there is a sequence which follows these rules:

None of the people have their arms raised at first Firstly, a person raises 1 hand; then they raise the second hand;
after that they put both hands down - these steps form a cycle Person #1 performs these steps all the time,
person #2 advances only after person #1 puts their hands down, and person #3 advances only after person #2 puts their
hands down """





def get_positions(n:int):
    first_person=0
    second_person=0
    third_person=0
    for i in range(n):
        if first_person<3:
            first_person+=1
            if first_person==3:
                second_person+=1
                first_person=0
                if second_person==3:
                    third_person+=1
                    second_person=0
                    if third_person==3:
                        third_person=0
    return print(first_person, second_person, third_person)

# def get_positions(n:int):
#     return (n%3,(n//3)%3,((n//3)//3)%3)


if __name__=='__main__':
    get_positions(54)