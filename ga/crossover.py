from random import randint
from enum import Enum


class CrossoverType(Enum):
    SINGLE_POINT = 0
    MULTI_POINT = 1
    UNIFORM = 2
    CYCLE = 3
    PMX = 4


class Crossover:
    def __init__(self, crossover_type: CrossoverType):
        self.__offspring = []
        self.__p1 = []
        self.__p2 = []
        self.__crossover_type = crossover_type


    # makes a crossover according to the type
    def perform(self, parent1: list, parent2: list, points=0) -> list:
        self.__p1 = parent1
        self.__p2 = parent2

        if len(parent1) != len(parent2):
            raise ValueError(f"Parents' length should be the same! You have: {len(parent1)} and {len(parent2)}")

        if self.__crossover_type == CrossoverType.SINGLE_POINT:
            self.__multi_point(1)

        elif self.__crossover_type == CrossoverType.MULTI_POINT:
            if points <= 0:
                raise ValueError("Wrong points count! Change an amount of the points or use another crossover.")
            self.__multi_point(points)

        elif self.__crossover_type == CrossoverType.UNIFORM:
            self.__uniform_crossover()
        
        elif self.__crossover_type == CrossoverType.CYCLE:
            self.__cycle_crossover()
        
        elif self.__crossover_type == CrossoverType.PMX:
            self.__pmx_crossover()
        
        else:
            raise TypeError(f"Non-existing crossover type: {self.__crossover_type}")
        
        return self.__offspring


    # crossover type setter
    def set_type(self, new_type: CrossoverType):
        self.__crossover_type = new_type


    ### Typical crossovers ###
    # performs n-point (or multi-point) crossover
    def __multi_point(self, points: int):
        prev_p = 0
        self.__offspring = []

        for i in range(points):
            p = randint(prev_p+1, len(self.__p1)-points+i)
            self.__offspring += self.__p2[prev_p:p] if i%2 else self.__p1[prev_p:p]
            prev_p = p

        self.__offspring += self.__p2[prev_p:] if points%2 else self.__p1[prev_p:]


    # performs uniform crossover
    def __uniform_crossover(self):
        mask = [randint(0, 1) for _ in range(len(self.__p1))]
        self.__offspring = [self.__p2[i] if mask[i] else self.__p1[i] for i in range(len(self.__p1))]

    
    ### Crossovers for the TSP-like problems, elements should be ordered anyhow ###
    ### Related to the cycle crossover ###
    # identifies cycles
    def __generate_cycle(self, idx: int) -> list:
        result = [self.__p1[idx], self.__p2[idx]]

        while result[-1] != result[0]:
            result.append(self.__p2[self.__p1.index(result[-1])])

        return result[:-1]

    
    # defines if the gene is in an odd or even cycle
    def __is_odd_cycle(self, gene, cycles: list) -> bool:
        for i, cycle in enumerate(cycles):
            if gene in cycle:
                return bool(i%2)


    # performs cycle crossover
    def __cycle_crossover(self):
        used_genes = []
        cycles = []

        for idx, gene in enumerate(self.__p1):
            if gene not in used_genes:
                cycle = self.__generate_cycle(idx)
                cycles.append(cycle)
                used_genes += cycle
        
        self.__offspring = [g2 if self.__is_odd_cycle(g1, cycles) else g1 for g1, g2 in zip(self.__p1, self.__p2)]

    
    ### Related to the partially mapped crossover ###
    # finds a random subset
    def __find_subset(self) -> tuple:
        start = randint(0, len(self.__p1)-2)
        end = randint(start+2, len(self.__p1))

        return start, end

    
    # finds a place for a gene from the subset of the second parent
    def __place_from_subset(self, idx: int, subset: tuple) -> int:
        new_idx = self.__p2.index(self.__p1[idx])

        if new_idx in range(*subset):
            return self.__place_from_subset(new_idx, subset)
        return new_idx


    # performs pmx crossover
    def __pmx_crossover(self):
        start, end = self.__find_subset()
        self.__offspring = [0]*start + self.__p1[start:end] + [0]*len(self.__p1[end:])

        for i, gene in enumerate(self.__p2):
            new_idx = i

            if gene in self.__offspring:
                continue
            elif i in range(start, end):
                new_idx = self.__place_from_subset(i, (start, end))

            self.__offspring[new_idx] = gene