"""Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of
n3 n^3n 3 , the cube above will have volume of (n−1)3 (n-1)^3(n−1) 3 and so on until the top which will have a volume
of 13 1^31 3 .

You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to
build?

The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be an integer m and you have to return the
integer n such as n3+(n−1)3+(n−2)3+...+13=m n^3 + (n-1)^3 + (n-2)^3 + ... + 1^3 = mn 3 +(n−1) 3 +(n−2) 3 +...+1 3 =m
if such a n exists or -1 if there is no such n. """


def find_nb(m: int) -> int:
    counter=0
    n=1
    while counter<=m:
        counter += n ** 3
        if counter == m:
            return n
        n += 1
    return -1


if __name__ == "__main__":
    assert find_nb(4183059834009) == 2022
