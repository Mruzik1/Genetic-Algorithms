from ga import GeneticAlgorithm, MutationType, CrossoverType
from tsp import NodesGenerator
import matplotlib.pyplot as plt


# generate / upload tsp sample
nodes_generator = NodesGenerator(30, saved_axis='./data/axis.txt')

primal_nodes = nodes_generator.get_nodes_list('./data/distances.txt')
print(*primal_nodes, '\n\n')


# initialize genetic algorithms with different params
ga1 = GeneticAlgorithm(0.1, CrossoverType.PMX, MutationType.INVERSION, fitness_function=nodes_generator.total_cost)
ga1.init_population(50, primal_nodes)
final_path1 = ga1.start(600, 20)

ga2 = GeneticAlgorithm(0.1, CrossoverType.PMX, MutationType.INVERSION, fitness_function=nodes_generator.total_cost)
ga2.init_population(50, primal_nodes)
final_path2 = ga2.start(600, 20)


# draw plots
# fig, axs = plt.subplots(2)

# axs[0].set_title('GA1')
# axs[0].plot(ga1.history)

# axs[1].set_title('GA2')
# axs[1].plot(ga2.history)

# for ax in axs:
#     ax.set(xlabel='pop number', ylabel='mean fitness score')

fig, ax = plt.subplots()
ax.plot(ga1.history)
ax.plot(ga2.history)
ax.legend(['GA1', 'GA2'])
ax.set(xlabel='pop number', ylabel='mean fitness score')

plt.show()


# draw the paths
# nodes_generator.draw_path(final_path1)
# nodes_generator.draw_path(final_path2)