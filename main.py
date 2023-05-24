from chromosome import Chromosome
from population import Population

def genetic_algorithm(population: Population) -> Chromosome:
    limit = 300
    while not population.solution_found() and limit:
        population.recombine()
        population.select()
        population.mutate()
        limit -= 1
    if population.solution_found():
        return max(population.chromosomes)
    return None

def main():
    population = Population(16, 500, 0.8)
    print(genetic_algorithm(population))

if __name__ == '__main__':
    main()