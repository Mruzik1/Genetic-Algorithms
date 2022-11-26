from ga import Crossover
from ga import Mutation
from random import shuffle


crossover = Crossover()
mutation = Mutation(1)


# parents
a = ['0']*50
b = ['1']*50

print('\nRegular crossovers:')
print(''.join(a))
print(''.join(b), '\n')

# N-point crossover (can be every number from 1 to the chromosomes_length - 1)
points = 5
crossover.n_point(a, b, points)
print(f"{points}-point crossover: {''.join(crossover.get_offspring())}")

# Single point crossover
crossover.n_point(a, b, 1)
print(f"Single point crossover: {''.join(crossover.get_offspring())}")

# Uniform crossover
crossover.uniform_crossover(a, b)
print(f"Uniform crossover: {''.join(crossover.get_offspring())}")


# Different mutations
mutation.set_offspring(list(range(1, 10)))
print('\nMutations performed on the range from 1 to 9')
print(f"Inversion (random subtour): {mutation.inversion()}")
print(f"Replace (random subtour):   {mutation.replace()}")


# Special crossovers
# parents
a = list(range(1, 15))
b = list(a)
shuffle(b)

print('\nCrossovers for ordered chromosomes (good for solving problems with graphs):')
print(a)
print(b, '\n')


# Cycle crossover
crossover.cycle_crossover(a, b)
print(f"Cycle crossover: {crossover.get_offspring()}")

# PMX crossover
crossover.pmg_crossover(a, b)
print(f"Partially mapped crossover: {crossover.get_offspring()}")