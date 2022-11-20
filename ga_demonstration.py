from ga import Crossover
from ga import Mutation
from random import shuffle


crossover = Crossover()
mutation = Mutation(1/9)


a = ['0']*50
b = ['1']*50

print('\nRegular crossovers:')
print(''.join(a))
print(''.join(b), '\n')

# N-point crossover (could be every number from 1 to the chromosomes_length - 1)
points = 5
crossover.n_point(a, b, points)
print(f"{points}-point crossover: {''.join(crossover.get_offspring())}")

# Single point crossover
crossover.n_point(a, b, 1)
print(f"Single point crossover: {''.join(crossover.get_offspring())}")

# Uniform crossover
crossover.uniform_crossover(a, b)
print(f"Uniform crossover: {''.join(crossover.get_offspring())}")

# Try mutation
mutation.set_offspring(list(range(1, 10)))
print('\nMutations performed on the range from 1 to 9 (chance of the mutation is 1/offspring_length)')
print(f"Inversion (2 elements): {mutation.inversion()}")
print(f"Replace (1 element):    {mutation.replace()}")


# Cycle-like crossover demonstration (uses while solving TSP for instance)
a = '1234567890abcdefghijklmnopqrstuvwxyz'.upper()
b = list(a)
shuffle(b)
b = ''.join(b)

print("\nCycle-like crossover (for TSP and similar, genes must be ordered):")
print(a)
print(b, '\n')

# Cycle crossover
crossover.cycle_crossover(list(a), list(b))
print(f"Cycle crossover: {''.join(crossover.get_offspring())}")