import random

        
def roulette_wheel_selection(population,popsize):
    
    fitness_sum=0
    for i in range(popsize):
        fitness_sum+=population[i].fitness_score
    r=random.randint(0,fitness_sum)
    s=0
    for i in range(popsize):
        if s<=r:
            s=population[i].fitness_score
        else:
            break

    return population[i]


