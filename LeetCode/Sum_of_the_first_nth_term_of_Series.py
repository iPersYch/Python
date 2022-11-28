def series_sum(n):
    counter=0
    i=0
    j=1
    while i!=n:
        counter+=1/j
        j+=3
        i=i+1
    return '{:.2f}'.format(counter)

print(series_sum(78))