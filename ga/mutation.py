from random import randint, random


class Mutation:
    def __init__(self, chance: float):
        self.__offspring = []
        self.__chance = chance

    
    # offspring setter
    def set_offspring(self, offspring: list):
        self.__offspring = offspring


    # finds a random subset
    def __find_subset(self) -> tuple:
        if len(self.__offspring) and random() < self.__chance:
            start = randint(0, len(self.__offspring)-2)
            end = randint(start+2, len(self.__offspring))

            return start, end
        return tuple()


    # random subset inversion (chance is 1/offsping_length)
    def inversion(self) -> list:
        tmp_offspring = self.__offspring.copy()
        subset = self.__find_subset()

        if len(subset):
            start, end = subset
            tmp_offspring = tmp_offspring[:start] + list(reversed(tmp_offspring[start:end])) + tmp_offspring[end:]

        return tmp_offspring

    
    # shifts genes to the left (chance is 1/offsping_length)
    def replace(self) -> list:
        tmp_offspring = self.__offspring.copy()
        subset = self.__find_subset()

        if len(subset):
            shift = randint(0, len(tmp_offspring))
            for i in range(*subset):
                tmp_offspring.insert(i-shift, tmp_offspring.pop(i))

        return tmp_offspring