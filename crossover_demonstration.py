from ga import Crossover
from random import shuffle


crossover = Crossover()


a = ['=']*50
b = ['-']*50

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


# Cycle-like crossover demonstration (uses while solving TSP for instance)
a = '1234567890abcdefghijklmnopqrstuvwxyz'.upper()
b = list(a)
shuffle(b)
b = ''.join(b)

print("\nCycle-like crossovers (for TSP and similar, genes mustn't repeat):")
print(a)
print(b, '\n')

# Cycle crossover
crossover.cycle_crossover(list(a), list(b))
print(f"Cycle crossover: {''.join(crossover.get_offspring())}")