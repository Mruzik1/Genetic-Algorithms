from ga import GeneticAlgorithm
from tsp import NodesGenerator


nodes_generator = NodesGenerator(30, saved_axis='./data/axis.txt')
# nodes_generator.generate_file('./data/distances.txt')
# nodes_generator.save_axis('./data/axis.txt')

primal_nodes = nodes_generator.get_nodes_list('./data/distances.txt')

print(*primal_nodes, '\n\n')

ga = GeneticAlgorithm(0.1, nodes_generator.total_cost)
ga.init_population(50, primal_nodes)
final_path = ga.start(2000, 10)

print('\n\n\n', *final_path)

nodes_generator.draw_path(final_path)