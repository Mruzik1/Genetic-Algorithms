from ga import GeneticAlgorithm
from tsp import NodesGenerator
from random import shuffle


nodes_generator = NodesGenerator(20)
# nodes_generator.generate_file('./data/distances.txt')

primal_nodes = nodes_generator.get_nodes_list('./data/distances.txt')

print(*primal_nodes, '\n\n')


ga = GeneticAlgorithm(1/len(primal_nodes), nodes_generator.total_cost)
ga.init_population(50, primal_nodes)
final_pop = ga.start(2500, 10)

print('\n\n\n', *final_pop)