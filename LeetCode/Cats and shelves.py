def solution(start, finish):
    if start==finish:
        return 0
    counter=0
    while start<finish:
        counter+=1
        start+=1
        if start==finish:
            return counter
        else:
            start+=2
            if start==finish:
                return counter
            if start>finish:
                start-=2

def solution(start, finish):
    n = finish - start
    return n // 3 + n % 3