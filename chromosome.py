from random import randint
import numpy as np
from math import ceil

class Chromosome:
    def __init__(self, n):
        self.n = n
        self.s = np.random.randint(n, size=n)
    
    def reproduce(self, other):
        crossover_point = randint(1, self.n - 1)
        child = Chromosome(self.n)
        child.s = np.concatenate((self.s[:crossover_point], other.s[crossover_point:]), axis=None)
        return child
    
    def fitness(self) -> int:
        total_pairs = self.n * (self.n - 1) / 2
        attackings = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.s[i] == self.s[j]: # row attackings
                    attackings += 1
                if abs(i - j) == abs(self.s[i] - self.s[j]): # column attackings
                    attackings += 1
        return (total_pairs - attackings) / total_pairs
    
    def __repr__(self):
        return str(self.s)
    
    def __lt__(self, other):
        return self.fitness() < other.fitness()

if __name__ == '__main__':
    ch1 = Chromosome(4)
    print(ch1)
    ch2 = Chromosome(4)
    print(ch2)
    ch3 = ch1.reproduce(ch2)
    print(ch3)