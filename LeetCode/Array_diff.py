def array_diff(a, b):
    return [x for x in a if x not in set(b)]


print(array_diff([1, 2, 2], [1]))
