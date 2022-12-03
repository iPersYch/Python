def bar_triang(point_a, point_b, point_c):
    x= sum(list(j for i,j in enumerate(point_a + point_b + point_c) if i%2==0 ))
    y= sum(list(j for i,j in enumerate(point_a + point_b + point_c) if i%2!=0 ))
    return [round(x/3,4),round(y/3,4)]