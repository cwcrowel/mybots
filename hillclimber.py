import constants as c
from solution import SOLUTION
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        print('parent weights: ', self.parent.weights)
        print('child weights: ', self.child.weights)
        print('parent fitness: ', self.parent.fitness)
        print('child fitness: ', self.child.fitness)


    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print("parent = " + str(self.parent.fitness) + " and child = " + str(self.child.fitness))