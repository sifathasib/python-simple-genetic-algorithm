import random

def one_point_crossover(p1,p2,target_len):


    
    c=random.randint(0,target_len)
    if c!= 0:
        temp=p1.values[c:]
        p1.values=p1.values[:c]+p2.values[c:]
        p2.values=p2.values[:c]+temp
    return p1,p2


