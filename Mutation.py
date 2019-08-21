
import random

alphabet='abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.,?:!1234567890'

def mutate(pop,target_len):
    for i in range(target_len):
        if pop.chek_list[i]==0:
            pop.values=pop.values[:i]+alphabet[random.randrange(len(alphabet))]+pop.values[(i+1):]

    return pop

