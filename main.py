from chromosome import Chromosome
from population import Population

def genetic_algorithm(population: Population) -> Chromosome:
    limit = 500
    while not population.solution_found() and limit:
        population.recombine()
        population.mutate()
        limit -= 1
    return max(population.chromosomes)

def main():
    population = Population(4, 6, 0.8)
    print(genetic_algorithm(population))

if __name__ == '__main__':
    main()