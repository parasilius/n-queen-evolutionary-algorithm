from nqueen import Population
from time import time

class GA:
    def __init__(self, n: int, population_size: int, mutation_rate: int) -> None:
        self.n = n
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = Population(self.n, self.population_size, self.mutation_rate)

    def run(self):
        limit = 300
        start_time = time()
        while not self.population.solution_found() and limit:
            self.population.recombine()
            self.population.select()
            self.population.mutate()
            limit -= 1
        print(f'executed for {(time() - start_time)}')
        if self.population.solution_found():
            return max(self.population.chromosomes)
        return None