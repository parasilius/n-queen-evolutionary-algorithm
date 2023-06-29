from random import randint
import numpy as np
from nqueen.board import Board

class Chromosome:
    def __init__(self, n):
        self.n = n
        self.s = np.random.randint(n, size=n)
    
    def reproduce(self, other):
        crossover_point = randint(1, self.n - 1)
        #crossover_point = ceil(self.n // 3) + 1
        child = Chromosome(self.n)
        child.s = np.concatenate((self.s[:crossover_point], other.s[crossover_point:]), axis=None)
        return child
    
    def fitness(self) -> float:
        total_pairs = self.n * (self.n - 1) / 2
        attackings = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.s[i] == self.s[j]: # row attackings
                    attackings += 1
                if abs(i - j) == abs(self.s[i] - self.s[j]): # cross attackings
                    attackings += 1
        return (total_pairs - attackings) / total_pairs

    def show(self):
        print(f'string is {self}.\nRepresentation:')
        for _ in range(4 * self.n):
            print('_', end='')
        print()
        for i in range(1, self.n + 1):
            for j in range(self.n):
                if self.n - i == self.s[j]:
                    print(' ♕ ', end='')
                else:
                    print('   ', end='')
                if j < self.n:
                    print('|', end='')
            if i < self.n:
                print()
                for _ in range(4 * self.n):
                    print('_', end='')
                print()
        print()
        for _ in range(4 * self.n):
            print('_', end='')
        print()
        board = Board(self.s)
        board.show()
    
    def __repr__(self):
        return str(self.s)
    
    def __lt__(self, other):
        return self.fitness() < other.fitness()

    def __le__(self, other):
        return self.fitness() <= other.fitness()

    def __eq__(self, other):
        return self.fitness() == other.fitness()

    def __gt__(self, other):
        return self.fitness() > other.fitness()

    def __ge__(self, other):
        return self.fitness() >= other.fitness()

if __name__ == '__main__':
    ch1 = Chromosome(4)
    print(ch1)
    ch2 = Chromosome(4)
    print(ch2)
    ch3 = ch1.reproduce(ch2)
    print(ch3)
