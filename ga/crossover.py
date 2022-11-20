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

    
    # identifies cycles
    def __generate_cycle(self, idx: int, p1: list, p2: list) -> list:
        result = [p1[idx], p2[idx]]

        while result[-1] != result[0]:
            result.append(p2[p1.index(result[-1])])

        return result[:-1]

    
    # defines if the gene is in the odd or even cycle
    def __is_odd_cycle(self, gene, cycles: list) -> bool:
        for i, cycle in enumerate(cycles):
            if gene in cycle:
                return bool(i%2)


    # performs cycle crossover (for TSP-like problems, elements should be the same)
    def cycle_crossover(self, parent1: list, parent2: list):
        used_genes = []
        cycles = []

        for idx, gene in enumerate(parent1):
            if gene not in used_genes:
                cycle = self.__generate_cycle(idx, parent1, parent2)
                cycles.append(cycle)
                used_genes += cycle
        
        self.__offspring = [g2 if self.__is_odd_cycle(g1, cycles) else g1 for g1, g2 in zip(parent1, parent2)]