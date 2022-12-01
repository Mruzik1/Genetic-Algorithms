from .crossover import Crossover, CrossoverType
from .mutation import Mutation, MutationType
from random import shuffle, choices


# created to solve only TSP (a minimization problem with ordered genes)
class GeneticAlgorithm:
    def __init__(self, mutation_chance: float, crossover_type: CrossoverType, mutation_type: MutationType, fitness_function):
        self.__crossover = Crossover(crossover_type)
        self.__mutation = Mutation(mutation_chance, mutation_type)
        self.__fit_func = fitness_function
        self.__population = []
        self.__pop_history = []
        self.__pop_size = 0


    # generates k chromosomes as an our first population, setups max population size
    def init_population(self, k: int, initial_chromosome: list):
        for _ in range(k):
            tmp_chromosome = initial_chromosome.copy()
            shuffle(tmp_chromosome)
            self.__population.append(tmp_chromosome)
        self.__pop_size = k


    # performs selection, sorts from the worst to the best (from maximum to minimum)
    # parameter "selector" is how many chromosomes with a bad score should be removed from the population
    def __selection(self, selector) -> int:
        self.__population.sort(key=lambda x: self.__fit_func(x), reverse=True)
        self.__population = self.__population[selector:]


    # returns a list of every element's fitness in the population
    def __get_fitness_scores(self) -> list:
        return [self.__fit_func(i) for i in self.__population]


    # choices 2 random parents from the population according to weights
    # because we have a minimizing problem, it's important to actualize the weights
    def __choice_parents(self) -> list:
        fit_scores = self.__get_fitness_scores()
        w = [float(i)**(-1)/sum(fit_scores) for i in fit_scores]
        
        return choices(self.__population, weights=w, k=2)


    # makes crossover k-times, generates offsprings
    def __perform_crossover(self, k: int):
        for _ in range(k):
            parent1, parent2 = self.__choice_parents()
            yield self.__crossover.perform(parent1, parent2, points=1)


    # generates mutated offsprings with some chance
    def __perform_mutation(self, offsprings):
        for i in offsprings:            
            yield self.__mutation.perform(i)


    # draws some parameters in the console while the algorithm is running
    def __print_info(self, population_num: int, k: int):
        current_minimum = min(self.__population, key=lambda x: self.__fit_func(x))

        print(f'Population: {population_num} / {k}\t \
                Current minimum: {self.__fit_func(current_minimum)}  ', end='\r')

        if (population_num+1) % (k // 5) == 0:
            print('\nCurrent population fitness: ', *self.__get_fitness_scores(), '\n')


    # population history getter
    # pop_history is a list of all mean population scores gotten during the algorithm's run
    @property
    def history(self) -> list:
        return self.__pop_history


    # returns population's mean fitness score
    def __get_mean(self):
        return sum(self.__get_fitness_scores())/self.__pop_size


    # starts learning
    # selector is a number of chromosomes that will be replaced by offsprings
    # k is an "evolving time/steps"
    # returns the best chromosome
    def start(self, k: int, selector: int) -> list:
        if selector >= self.__pop_size:
            raise ValueError(f"Selector should be less than the population size: {selector} >= {self.__pop_size}")

        for i in range(k):
            if k >= 5:
                self.__print_info(i, k)

            self.__selection(selector)

            offsprings = self.__perform_crossover(self.__pop_size-len(self.__population))
            offsprings = list(self.__perform_mutation(offsprings))

            self.__population += offsprings
            self.__pop_history.append(self.__get_mean())
        
        return min(self.__population, key=lambda x: self.__fit_func(x))