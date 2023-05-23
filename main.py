from chromosome import Chromosome
from population import Population

def genetic_algorithm(population: Population) -> Chromosome:
    while True:
        population.recombine()
        population.mutate()
    return population.sorted()[0]

def main():
    population = Population()
    print(genetic_algorithm(population))

if __name__ == '__main__':
    main()