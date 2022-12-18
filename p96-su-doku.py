'''
This is solved recursively: at each empty square, check if the current digit placement is valid
through the column, row and the 3x3 area. If the digit is valid there, then, fill out that square
and use the updated grid as the argument for the next iteration. If the function returns false,
this means the current digit placement is invalid, and the next digit is tried. The base case is
if all the squares are filled out, which the function returns true.
'''

infile = 'p96-su-doku.in'
ss = open(infile).read().split('\n')

def check_num(Gd, a, b, num):
    if any([Gd[x][b] == num for x in range(9)]):
        return False

    if Gd[a].count(num) != 0:
        return False

    for x in range(a//3 * 3, (a//3 + 1) * 3):
        for y in range(b//3 * 3, (b//3 + 1) * 3):
            if Gd[x][y] == num:
                return False

    Gd[a][b] = num
    return True

def solve_sudoku(Gd):
    for i in range(9):
        for j in range(9):
            if Gd[i][j] == 0:
                for k in range(1, 10):
                    if check_num(Gd, i, j, k) and solve_sudoku(Gd):
                        return True
                    else:
                        Gd[i][j] = 0

                return False
    return True

grid, ans = [], 0
for x in ss:
    if x.split(' ')[0] != 'Grid':
        grid.append(list(map(int, x)))
        if len(grid) == 9:
            solve_sudoku(grid)
            ans += int(''.join(map(str, grid[0][:3]))) 
            grid = []

print('The 3 digit number at the top left corner of the solved sudokus: {0}'.format(ans))