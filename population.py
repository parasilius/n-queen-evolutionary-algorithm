import numpy as np
from math import ceil
from random import randint
from chromosome import Chromosome

class Population:
    def __init__(self, n: int, population_size: int, mutation_rate: int):
        self.n = n
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        # creating initial population
        self.chromosomes = []
        for _ in range(population_size):
            self.chromosomes.append(Chromosome(self.n))

    def recombine(self) -> None:
        for i in range(0, self.n, 2):
            s1 = self.chromosomes[i].reproduce(self.chromosomes[i + 1])
            s2 = self.chromosomes[i + 1].reproduce(self.chromosomes[i])
            self.chromosomes.append(s1)
            self.chromosomes.append(s2)

    def mutate(self) -> None:
        sample_indices = np.random.choice(self.population_size, int(self.population_size * self.mutation_rate))
        for i in sample_indices:
            self.chromosomes[i].s[randint(0, self.n - 1)] = randint(0, self.n - 1)

    def select(self) -> None:
        self.chromosomes = self.chromosomes.sort()[:self.population_size]
    
    def solution_found(self) -> bool:
        return max(self.chromosomes) == 1.0

if __name__ == '__main__':
    p = Population(4, 2, 0.7)