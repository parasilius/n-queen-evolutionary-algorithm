from nqueen import GA

def main():
    ga = GA(11, 200, 0.8)
    if ga.n == 1:
        print('Solution to 1-queen is trivial! Just fill the empty cell!')
    elif ga.n == 2 or ga.n == 3:
        print('No solution exists for N = 2 or 3!')
    else:
        solution = ga.run()
        if solution:
            solution.show()
        else:
            print('No solution found! Please try again...')

if __name__ == '__main__':
    main()