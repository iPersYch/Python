def london_city_hacker(journey):
    jh = list(type(x) for x in journey)
    counter = 0
    while jh:
        if jh[0] == str:
            counter += 2.4
            jh = jh[1::]
        if len(jh)>1:
            if jh[0] == int and jh[1] == int:
                counter += 1.5
                jh = jh[2::]
        if len(jh) > 1:
            if jh[0] == int and jh[1] != int:
                counter += 1.5
                jh = jh[1::]
        if len(jh)==1 and jh[0]==int:
            counter+=1.5
            break
    return f'£{counter:.2f}'

if __name__ == "__main__":
    london_city_hacker(['Northern', 'Central', 'Circle'])