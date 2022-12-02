from ga import Crossover, Mutation, MutationType, CrossoverType
from random import shuffle


crossover = Crossover(CrossoverType.MULTI_POINT)
mutation = Mutation(1, MutationType.INVERSION)


## Regular crossovers
# parents
a = ['0']*50
b = ['1']*50
points = 5

print('\nRegular crossovers:')
print(''.join(a))
print(''.join(b), '\n')

# N-point crossover (can be every number from 1 to the chromosomes_length - 1)
print(f"{points}-point crossover: {''.join(crossover.perform(a, b, points=points))}")

# Single point crossover
crossover.set_type(CrossoverType.SINGLE_POINT)
print(f"Single point crossover: {''.join(crossover.perform(a, b))}")

# Uniform crossover
crossover.set_type(CrossoverType.UNIFORM)
print(f"Uniform crossover: {''.join(crossover.perform(a, b))}")


## Special crossovers
# parents
a = list(range(1, 15))
b = list(a)
shuffle(b)

print('\nCrossovers for ordered chromosomes (good for solving problems with graphs):')
print(a)
print(b, '\n')

# Cycle crossover
crossover.set_type(CrossoverType.CYCLE)
print(f"Cycle crossover: {crossover.perform(a, b)}")

# PMX crossover
crossover.set_type(CrossoverType.PMX)
print(f"Partially mapped crossover: {crossover.perform(a, b)}")


# Different mutations
print('\nMutations performed on the range from 1 to 9')
offspring = list(range(1, 10))

print(f"Inversion (random subtour): {mutation.perform(offspring)}")

mutation.set_type(MutationType.REPLACEMENT)
print(f"Replace (random subtour):   {mutation.perform(offspring)}")