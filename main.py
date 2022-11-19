from ga import Crossover
from tsp import NodesGenerator


crossover = Crossover([123, 345], [321, 456])
nodes_generator = NodesGenerator(10)

nodes_generator.generate_distances('./data/distances.txt')
nodes = nodes_generator.get_nodes_dict('./data/distances.txt')

nodes_generator.draw_algorithm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])