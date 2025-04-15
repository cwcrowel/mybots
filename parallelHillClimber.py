import constants as c
from solution import SOLUTION
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        #os.system('rm brain*.nndf')
        #os.system('rm fitness*.txt')

        self.parents = {}
        self.nextAvailableID = 0

        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        for i in self.parents.keys():
            print(f'child and parent fitness: ', self.children[i].fitness, self.parents[i].fitness)
        self.Select()

    def Spawn(self):
        self.children={}
        for key in self.parents.keys():
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID()
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children.values():
            child.Mutate()


    def Select(self):
        for key in self.parents.keys():
            if self.children[key].fitness > self.parents[key].fitness:  # Changed to > per steps 8-10 in Final Project to prefer higher fitness values
                self.parents[key] = self.children[key]

    def Print(self):
        print("\nparent = " + str(self.parent.fitness) + " and child = " + str(self.child.fitness))

    def Show_Best(self):
        lowest = -1000.0    # Changed to -1000 per steps 8-10 in Final Project
        lowest_parent = None
        for parent in self.parents.values():
            if parent.fitness > lowest: # Changed to > per steps 8-10 in Final Project
                lowest = parent.fitness
                lowest_parent = parent
        print('Final parent fitness: ', lowest_parent.fitness)
        lowest_parent.Start_Simulation('GUI')

    def Evaluate(self, solutions):
        for parent in solutions.values():
            parent.Start_Simulation('DIRECT')

        for parent in solutions.values():
            parent.Wait_For_Simulation_To_End()