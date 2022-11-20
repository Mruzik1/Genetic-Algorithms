from random import randint, choice, random


class Mutation:
    def __init__(self, chance: float):
        self.__offspring = []
        self.__chance = chance

    
    # offspring setter
    def set_offspring(self, offspring: list):
        self.__offspring = offspring


    # random two elements inversion (chance is 1/offsping_length)
    def inversion(self) -> list:
        tmp_offspring = self.__offspring.copy()

        if len(self.__offspring) and random() < self.__chance:
            start = randint(0, len(tmp_offspring)-1)
            end = start+1 if start+1 < len(tmp_offspring) else 0

            tmp_offspring[start], tmp_offspring[end] = tmp_offspring[end], tmp_offspring[start]

        return tmp_offspring

    
    # changing gene's place (chance is 1/offsping_length)
    def replace(self) -> list:
        tmp_offspring = self.__offspring.copy()

        if len(self.__offspring) and random() < self.__chance:
            old_idx = randint(0, len(tmp_offspring)-1)
            idx = choice(list(set(range(len(tmp_offspring))) ^ {old_idx}))

            tmp_offspring.insert(idx, tmp_offspring.pop(old_idx))

        return tmp_offspring
