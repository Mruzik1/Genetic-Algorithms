from random import randint, random
from enum import Enum


class MutationType(Enum):
    INVERTION = 0
    REPLACEMENT = 1


class Mutation:
    def __init__(self, chance: float, mutation_type: MutationType):
        self.__offspring = []
        self.__chance = chance
        self.__mutation_type = mutation_type


    # makes a mutation according to the mutation_type
    # returns a new offspring if everything is ok, an error otherwise
    def perform(self, offspring: list) -> list:
        self.__offspring = offspring

        if random() > self.__chance:
            return offspring

        if self.__mutation_type == MutationType.INVERTION:
            return self.__inversion()

        elif self.__mutation_type == MutationType.REPLACEMENT:
            return self.__replace()

        else:
            raise TypeError(f"Non-existing mutation type: {self.__mutation_type}")

    
    # mutation type setter
    def set_type(self, new_type: MutationType):
        self.__mutation_type = new_type


    # finds a random subset
    def __find_subset(self) -> tuple:
        start = randint(0, len(self.__offspring)-2)
        end = randint(start+2, len(self.__offspring))

        return start, end


    # random subset inversion (chance is 1/offsping_length)
    def __inversion(self) -> list:
        tmp_offspring = self.__offspring.copy()
        subset = self.__find_subset()

        start, end = subset
        tmp_offspring = tmp_offspring[:start] + list(reversed(tmp_offspring[start:end])) + tmp_offspring[end:]

        return tmp_offspring

    
    # shifts genes to the left (chance is 1/offsping_length, random step)
    def __replace(self) -> list:
        tmp_offspring = self.__offspring.copy()
        subset = self.__find_subset()

        shift = randint(0, len(tmp_offspring))
        for i in range(*subset):
            tmp_offspring.insert(i-shift, tmp_offspring.pop(i))

        return tmp_offspring