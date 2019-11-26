import time
import sys

class NQueensBacktracking:

    def __init__(self, n=8, demo=False):
        self.demo = demo
        self.n = n
        self.queen = [0] * (n+1)
        self.row = [0] * (n+1)
        self.hdia = [0] * (2*n + 1)
        self.ndia = [0] * (2*n + 1)
        self.sol_count = 0
        self.solutions = []


    def printBoard(self, column=0):
        print()
        #i = self.n
        for i in range(1, self.n+1):
            for j in range(1, self.n+1):
                symbol = "_ "
                if (self.row[i] or self.hdia[i+j] or self.ndia[j-i+(self.n-1)] or j <= column):
                    symbol = "x  "
                if (self.queen[j] == i):
                    symbol = "Q  "
                print(symbol, end='')
            print()
            i -= 1
        print()

    def sleep_a_bit(self):
        time.sleep(0.1)

    def place_queen(self, x):
        n = self.n
        for y in range (1, self.n+1):
            if (not(self.row[y] or self.hdia[x+y] or self.ndia[x-y+(n-1)])):
                # place Queen and all threatened fields (reachabele by the placed queen)
                self.queen[x] = y
                self.row[y] = True
                self.hdia[x+y] = True
                self.ndia[x-y+(n-1)] = True
                if (self.demo):
                    self.sleep_a_bit()
                    print("Queen placed on (" + str(x) + "," + str(y) + ")")
                    self.printBoard(x)
                if (x < n): # Still empty columns - make recursion (x+1)
                    self.place_queen (x+1)
                else:  # All columns occupied - solution found
                    self.sol_count += 1
                    sol_coordinates = []
                    for i in range (1, n+1):
                        sol_coordinates.append([i, self.queen[i]])
                    self.solutions.append(sol_coordinates)
                    print(f"Solution #{self.sol_count} found:")
                    print(sol_coordinates)
                    self.printBoard()
                # Backtracking - Release previously occupied fields
                self.queen[x] = 0
                self.row[y] = False
                self.hdia[x+y] = False
                self.ndia[x-y+(n-1)] = False
                if (self.demo):
                    self.sleep_a_bit()
                    print("Queen removed from (" + str(x) + "," + str(y) + ")", end='')
                    self.printBoard(x-1)
        return True

if __name__ == "__main__":
    # get arguments from command line
    try:
        n = int(sys.argv[1])
    except IndexError:
        n = 8
    try:
        demo = int(sys.argv[2])
    except IndexError:
        demo = False

    # instantiate class and run backtracking algo
    print(f"Using board size {n}")
    print("DEMO mode is ", end="")
    print("On" if demo else "Off")
    myqueens = NQueensBacktracking(n, demo)
    myqueens.place_queen(1)
    if demo:
        print("Total solutions:", myqueens.sol_count)
        for sol in  myqueens.solutions:
            print(sol)
