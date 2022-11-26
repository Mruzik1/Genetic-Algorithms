from random import randint


class Crossover:
    def __init__(self):
        self.__offspring = []


    ### Typical crossovers ###
    # getting the offspring
    def get_offspring(self) -> list:
        return self.__offspring


    # performs n-point (or multi-point) crossover
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

    
    ### Crossovers for the TSP-like problems, elements should be ordered anyhow ###
    ### Related to the cycle crossover ###
    # identifies cycles
    def __generate_cycle(self, idx: int, p1: list, p2: list) -> list:
        result = [p1[idx], p2[idx]]

        while result[-1] != result[0]:
            result.append(p2[p1.index(result[-1])])

        return result[:-1]

    
    # defines if the gene is in an odd or even cycle
    def __is_odd_cycle(self, gene, cycles: list) -> bool:
        for i, cycle in enumerate(cycles):
            if gene in cycle:
                return bool(i%2)


    # performs cycle crossover
    def cycle_crossover(self, parent1: list, parent2: list):
        used_genes = []
        cycles = []

        for idx, gene in enumerate(parent1):
            if gene not in used_genes:
                cycle = self.__generate_cycle(idx, parent1, parent2)
                cycles.append(cycle)
                used_genes += cycle
        
        self.__offspring = [g2 if self.__is_odd_cycle(g1, cycles) else g1 for g1, g2 in zip(parent1, parent2)]

    
    ### Related to the partially mapped crossover ###
    # finds a random subset
    def __find_subset(self, parents_length: int) -> tuple:
        start = randint(0, parents_length-2)
        end = randint(start+2, parents_length)

        return start, end

    
    # finds a place for gene from the subset of the second parent
    def __place_from_subset(self, p1: list, p2: list, idx: int, subset: tuple) -> int:
        new_idx = p2.index(p1[idx])

        if new_idx in range(*subset):
            return self.__place_from_subset(p1, p2, new_idx, subset)
        return new_idx


    # performs pmx crossover
    def pmx_crossover(self, parent1: list, parent2: list):
        start, end = self.__find_subset(len(parent1))
        self.__offspring = [0]*start + parent1[start:end] + [0]*len(parent1[end:])

        for i, gene in enumerate(parent2):
            new_idx = i

            if gene in self.__offspring:
                continue
            elif i in range(start, end):
                new_idx = self.__place_from_subset(parent1, parent2, i, (start, end))

            self.__offspring[new_idx] = gene