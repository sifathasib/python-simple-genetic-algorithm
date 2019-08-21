
import random
from Selection import roulette_wheel_selection
from Mutation import mutate
from CrossOver import one_point_crossover

alphabet='abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.,?:!1234567890'
target_string ='Hello World!My name is sifat.I have just sucessfully implemented Genetic Algorithm.My contact:01756359508'
target_len=len(target_string)

def string_generator(target_len):
    strng=''
    for i in range(target_len):
        strng+=alphabet[random.randrange(len(alphabet))]
    return strng

def fitness(string):
    chek_list=[0 for i in range(target_len)]
    score=0
    for i in range(target_len): 
        if chek_list[i]==0 and string[i]==target_string[i]:
            chek_list[i]=1
            score+=1
    return chek_list,score

class pop:
    values=''
    chek_list=[]
    fitness_score=0
    
popsize=10
population={}
Best=pop()
counter=0
#randomly first solution generate
for i in range(popsize): 
    population[i]=pop()
    population[i].values=string_generator(target_len)
    population[i].chek_list,population[i].fitness_score=fitness(population[i].values)

    if Best.fitness_score==0 or population[i].fitness_score > Best.fitness_score:
        Best=population[i]

Counter=0
while Best.fitness_score != target_len:
    for i in range(popsize): 
        population[i].chek_list,population[i].fitness_score=fitness(population[i].values)
        if Best.fitness_score==0 or population[i].fitness_score > Best.fitness_score:
            Best=population[i]
    print(Best.values)
    print(Best.chek_list)
    print(Best.fitness_score)
    Q={}
    for i in range(int(popsize/2)):
        parent1=roulette_wheel_selection(population,popsize)
        parent2=roulette_wheel_selection(population,popsize)

        children1,children2=one_point_crossover(parent1,parent2,target_len)

        children1= mutate(children1,target_len)
        children2= mutate(children2,target_len)

        Q[2*i]=children1
        Q[(2*i)+1]=children2

    population=Q
    Counter+=1
    
print(Best.values)
print(Best.chek_list)
print(Best.fitness_score)
print('Loop number:',Counter)




























    
