import numpy as np


class Crossover:
    def __init__(self, parent1, parent2):
        self.__parent1 = parent1
        self.__parent2 = parent2
        self.__offspring = np.array([])