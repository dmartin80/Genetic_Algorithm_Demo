#imports
import random
import math
import Direction_Vector as DV
import copy

class brain:
    def __init__(self):
        self.direction_length = 250
        self.brain_step = 0
        self.directions = []
        self.randomize()

    def randomize(self):
        for i in range(self.direction_length):
            rand_angle = (random.randint(0,359)*math.pi)/180
            self.directions.append(DV.vector(0, 0))
            self.directions[i].from_angle(rand_angle)
    
    def clone(self, parent):
        self.directions = copy.deepcopy(parent.brain.directions)

    def mutate(self, gen):
        mutation_rate = 0.01/(0.5 *gen)
        for i in range(self.direction_length):
            rand = random.uniform(0, 1)
            if rand <= mutation_rate:
                rand_angle = (random.randint(0,359)*math.pi)/180
                self.directions[i].from_angle(rand_angle)
