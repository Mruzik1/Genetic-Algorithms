from ga import Crossover
from tsp import NodesGenerator


nodes_generator = NodesGenerator(20)
nodes_generator.generate_file('./data/distances.txt')

nodes1 = nodes_generator.get_nodes_list('./data/distances.txt')
nodes2 = list(reversed(nodes1))