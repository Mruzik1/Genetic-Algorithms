from random import randint


class Crossover:
    def __init__(self):
        self.__offspring = []


    # getting the offspring
    def get_offspring(self) -> list:
        return self.__offspring


    # performs n-point crossover
    def n_point(self, parent1: list, parent2: list, points: int):
        prev_p = 0
        self.__offspring = []

        for i in range(points):
            p = randint(prev_p+1, len(parent1)-points+i)
            self.__offspring += parent2[prev_p:p] if i%2 else parent1[prev_p:p]
            prev_p = p

        self.__offspring += parent2[prev_p:] if points%2 else parent1[prev_p:]


    # performs uniform crossover
    def uniform_crossover(self, parent1: list, parent2: list):
        mask = [randint(0, 1) for _ in range(len(parent1))]
        self.__offspring = [parent2[i] if mask[i] else parent1[i] for i in range(len(parent1))]