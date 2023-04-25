import Dot
import random
import copy

num_dots = 300
dot_list = []
fitness_sum = 0
gen = 1
best_dot = 0

for i in range(num_dots):
    dot_list.append(Dot.dot())

def all_dots_done():
    for i in dot_list:
        if not i.dead  and not i.reached_goal:
            return False
    return True

def calculate_fitness():
    for i in dot_list:
        i.calculate_fitness()
        calc_fitness_sum()
        get_best_dot()

def calc_fitness_sum():
    global fitness_sum
    fitness_sum = 0
    for i in dot_list:
        fitness_sum += i.fitness

def get_best_dot():
    global best_dot
    best_dot = 0
    for i in range(num_dots-1):
        if dot_list[i].fitness > dot_list[best_dot].fitness:
            best_dot = i

def get_parent():
    global fitness_sum, dot_list    
    rand = random.uniform(0, fitness_sum)
    running_sum = 0
    for i in dot_list:
        running_sum += i.fitness
        if running_sum > rand:
            return i
    return None

def selection():
    global dot_list, num_dots, gen, best_dot
    next_gen_dots = []
    next_gen_dots.append(Dot.dot())
    next_gen_dots[0].clone_brain(dot_list[best_dot])
    next_gen_dots[0].set_best_dot()
    for i in range(num_dots-1):
        parent = get_parent()            
        next_gen_dots.append(Dot.dot())
        next_gen_dots[i+1].clone_brain(parent)
    dot_list = copy.deepcopy(next_gen_dots)
    gen += 1

def mutate():
    global num_dots, dot_list, gen
    for i in range(num_dots-1):
        dot_list[i+1].brain.mutate(gen)

def next_gen():
    calculate_fitness()
    selection()
    mutate()


