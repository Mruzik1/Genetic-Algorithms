from random import randint


class Crossover:
    def __init__(self):
        self.__offspring = []


    # getting the offspring
    def get_offspring(self) -> list:
        return self.__offspring
    

    # performs single point crossover
    def single_point(self, parent1: list, parent2: list):
        point = randint(1, len(parent1)-1)
        self.__offspring = parent1[:point] + parent2[point:]


    # performs n-point crossover
    def n_point(self, parent1: list, parent2: list, points: int):
        if points >= len(parent1) or points < 1:
            raise ValueError(f"Wrong points count: {points}.")
        
        prev_p = 0
        for i in range(points):
            p = randint(prev_p+1, len(parent1)-points+i)
            self.__offspring += parent2[prev_p:p] if i%2 else parent1[prev_p:p]
            prev_p = p

        self.__offspring += parent2[prev_p:] if points%2 else parent1[prev_p:]