from ga import Crossover


crossover = Crossover()

a = ['=']*50
b = ['-']*50

print(''.join(a))
print(''.join(b), '\n')

points = 5
crossover.n_point(a, b, points)
print(f"{points}-point crossover: {''.join(crossover.get_offspring())}")

crossover.single_point(a, b)
print(f"Single point crossover: {''.join(crossover.get_offspring())}")