from ga import Crossover
from tsp import NodesGenerator
from random import shuffle


nodes_generator = NodesGenerator(20)
# nodes_generator.generate_file('./data/distances.txt')

nodes1 = nodes_generator.get_nodes_list('./data/distances.txt')
nodes2 = nodes1.copy()
shuffle(nodes2)

print(*nodes1)
print(*nodes2)


crossover = Crossover()
crossover.cycle_crossover(nodes1, nodes2)
print(*crossover.get_offspring())