from .crossover import Crossover
from .mutation import Mutation
from random import shuffle, choices


class GeneticAlgorithm:
    def __init__(self, mutation_chance: float, fitness_function):
        self.__crossover = Crossover()
        self.__mutation = Mutation(mutation_chance)
        self.__fit_func = fitness_function
        self.__population = []
        self.__pop_size = 0


    # generates k chromosomes as an our first population, setups max population size
    def init_population(self, k: int, primal_chromosome: list):
        for _ in range(k):
            tmp_chromosome = primal_chromosome.copy()
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
        w = [(sum(fit_scores))//i for i in fit_scores]
        
        return choices(self.__population, weights=w, k=2)


    # makes crossover k-times, generates offsprings
    def __perform_crossover(self, k: int):
        for _ in range(k):
            parent1, parent2 = self.__choice_parents()
            self.__crossover.cycle_crossover(parent1, parent2)
            
            yield self.__crossover.get_offspring()

    
    # generates mutated offsprings with some chance (usually 1/len(population))
    def __perform_mutation(self, offsprings):
        for i in offsprings:
            self.__mutation.set_offspring(i)
            
            yield self.__mutation.inversion()


    # draws some parameters in the console while the algorithm is running
    def __draw_info(self, population_n: int, k: int):
        current_minimum = min(self.__population, key=lambda x: self.__fit_func(x))

        print(f'Population: {population_n} / {k}\t \
                Current minimum: {self.__fit_func(current_minimum)}', end='\r')

        if population_n % (k // 5) == 0:
            print('\n', *current_minimum, '\n')


    # starts learning
    def start(self, k: int, selector: int) -> list:
        for i in range(k):
            self.__draw_info(i, k)

            self.__selection(selector)

            offsprings = self.__perform_crossover(self.__pop_size-len(self.__population))
            offsprings = list(self.__perform_mutation(offsprings))

            self.__population += offsprings
        
        return min(self.__population, key=lambda x: self.__fit_func(x))