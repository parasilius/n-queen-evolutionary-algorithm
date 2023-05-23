import numpy as np
from math import ceil
from random import rnd
from chromosome import Chromosome

class Population:
    def __init__(self, n: int, population_size: int, mutation_rate: int):
        self.n = n
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        # creating initial population
        self.population = []
        for _ in range(population_size):
            self.population.append(Chromosome(self.n))

    def recombine(self) -> None:
        for i in range(0, self.n, 2):
            s1 = self.reproduce(self.population[i], self.population[i + 1])
            s2 = self.reproduce(self.population[i + 1], self.population[i])
            self.population.append(s1, s2)

    def mutate(self) -> None:
        sample_indices = np.random.choice(self.population_size, int(self.population_size * self.mutation_rate))
        for i in sample_indices:
            self.population[i][rnd(0, self.n - 1)] = rnd(0, self.n - 1)

if __name__ == '__main__':
    ga = Population(4, 2, 0.7)
    print(ga.recombine([1, 3, 2, 0], [0, 0, 1, 3]))