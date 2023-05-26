from chromosome import Chromosome
from population import Population
import time

def genetic_algorithm(population: Population) -> Chromosome:
    limit = 300
    start_time = time.time()
    while not population.solution_found() and limit:
        population.recombine()
        population.select()
        population.mutate()
        limit -= 1
    print(f'executed for {(time.time() - start_time)}')
    if population.solution_found():
        return max(population.chromosomes)
    return None

def main():
    population = Population(16, 200, 0.8)
    if population.n == 1:
        print('Solution to 1-queen is trivial! Just fill the empty cell!')
    elif population.n == 2 or population.n == 3:
        print('No solution exists for N = 2 or 3!')
    else:
        solution = genetic_algorithm(population)
        if solution:
            solution.show()
        else:
            print('No solution found! Please try again...')

if __name__ == '__main__':
    main()