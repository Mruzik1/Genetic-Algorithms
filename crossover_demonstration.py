from ga import Crossover


crossover = Crossover()

a = ['=']*50
b = ['-']*50

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