import argparse
import os

os.chdir("input")
# Arg for command line
parser = argparse.ArgumentParser()
for arg in {'--infile', '--outfile'}:
    parser.add_argument(arg, nargs='?', default=None, const=None)
args = parser.parse_args()


# This function returns a correct display for the complex number
def complex_printer(number):
    comp = complex(number)
    if comp.real != 0:
        if comp.imag != 0:
            return complex(round(comp.real, 4), round(comp.imag, 4))
        return comp.real
    return complex(0, round(comp.imag, 4)) if comp.imag != 0 else 0


# x+ay = 0 -> a = -(x / y)
# Useful for determining the
# coefficient to use to multiply a
# row before adding to another
def zero(x, y):
    return -(x / y)


# ax = 1 -> a = 1/x
# Useful for determining the
# coefficient to use to multiply a
# row to find 1 in pivot
def one(x):
    return 1 / x


class Matrice:
    # Constructor for matrix class
    def __init__(self, rows, column, cont):
        self.rows, self.columns = rows, column
        self.contents = cont


class SystemLinear:
    # The system in matrix form: aX = b
    def __init__(self, n, m, ab):
        self.ab = ab
        self.n, self.m = n, m
        # self.permutation to contain column swap and
        # self.counter to notice the presence of permutation
        self.permutation, self.counter = [], 0
        # if matrice is scaled
        self.echelon = False

    # A matrix
    @property
    def a(self):
        return [x[:self.n] for x in self.ab]

    # B vector
    @property
    def b(self):
        return [x[self.n] for x in self.ab]

    @property
    def rank(self):
        # To check if matrix is scaled
        if not self.echelon:
            return 'Non-scaled matrix'
        rank = self.m
        for x in self.a:
            if x == [0 for _ in range(self.n)]:
                rank -= 1
        return rank

    # multiply the line by the coefficient
    @staticmethod
    def multiply_line(line, coefficient):
        return [coefficient * x for x in line]

    # Return L1 + (coefficient)L2
    @staticmethod
    def add_line(line_1, line_2, coefficient):
        return [x + (coefficient * y) for x, y in zip(line_1, line_2)]

    # Do L[x]<->L[y]
    def swap_line(self, x, y):
        self.ab[x], self.ab[y] = self.ab[y], self.ab[x]

    # Do L[n][x]<->L[n][y]
    def swap_column(self, x, y):
        for n in range(self.n):
            self.ab[n][x], self.ab[n][y] = self.ab[n][y], self.ab[n][x]

    # To swap solutions
    def sol_permutation(self, solution):
        for x in self.permutation:
            temp = solution[x[0]]
            solution[x[0]] = solution[x[1]]
            solution[x[1]] = temp

    # To find the right pivot
    def null_pivot(self, x, base):
        if x == self.n - 1:
            return 0
        else:
            print(x)
            for z in range(x + 1, self.m):
                if self.ab[z][x] != 0:
                    print(f'L{x} <-> L{z}')
                    self.swap_line(base, z)
                    return 2
            for n in range(x + 1, self.n):
                if self.ab[x][n] != 0:
                    print(f'C{x}<-> C{n}')
                    self.swap_column(base, n)
                    self.permutation.append([x, n])
                    return 2
                self.null_pivot(x + 1, base)
        return 0

    def gauss_algorithm(self):
        for x in range(self.n):
            print('x:', x)
            if x + 1 > self.m - 1:
                break
            if self.ab[x][x] == 0:
                a = self.null_pivot(x, x)
                print('a;', a)
                if a == 0:
                    break
            self.ab[x] = SystemLinear.multiply_line(self.ab[x], one(self.ab[x][x]))
            for y in range(x + 1, self.m):
                print('y:', y)
                pivot = zero(self.ab[y][x], self.ab[x][x])
                print(f'L{y}<-L{y} +({pivot}) * L{x}')
                self.ab[y] = self.add_line(self.ab[y], self.ab[x], pivot)
        self.echelon = True

    def resolution(self):
        # Here we go back up triangular system
        # found to draw the solutions
        sol = [[0] for _ in range(self.n)]
        sol[self.n - 1] = [self.b[self.n - 1] / self.a[self.n - 1][self.n - 1]]
        for i in range(len(self.a) - 2, -1, -1):
            somme = 0
            for k in range(i + 1, self.n):
                somme += self.a[i][k] * sol[k][0]
            sol[i] = [(self.b[i] - somme) / self.a[i][i]]
        if self.counter != 0:
            self.sol_permutation(sol)
        sol = [[complex_printer(x[0])] for x in sol]
        return Matrice(self.n, 1, sol)

    @property
    def solution(self):
        print("Start solving the equation")
        self.gauss_algorithm()
        rank = self.rank
        print('Rang:', rank)
        if rank == self.m:
            if rank == self.n:
                return self.resolution()
            else:
                return 'Infinitely many solutions'
        if rank < self.m:
            for x in self.b[rank:]:
                if x != 0:
                    return 'No solutions'
            if rank == self.n:
                return self.resolution()
            else:
                return 'Infinitely many solutions'


with open(args.infile, 'r') as infile, open(args.outfile, 'w') as outfile:
    contents = []
    # We read the content in in.txt
    for q in infile:
        if q[-1] == '\n':
            contents.append(q[:-1].split())
        else:
            contents.append(q.split())
    # we turn the string content into float
    sys_mat = [[complex(x) for x in y] for y in contents[1:]]
    system_lin = SystemLinear(int(contents[0][0]), int((contents[0][1])), sys_mat)
    soluce = system_lin.solution
    if soluce == 'No solutions':
        outfile.write('No solutions')
        print(f'{soluce}')
    elif soluce == 'Infinitely many solutions':
        outfile.write('Infinitely many solutions')
        print(f'{soluce}')
    else:

        outfile.writelines(str(x[0]) + '\n' for x in soluce.contents)
        print(f'The solution is {soluce.contents}')
    print('Saved to out.txt')
