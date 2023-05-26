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
    population = Population(5, 300, 0.8)
    genetic_algorithm(population).show()

if __name__ == '__main__':
    main()