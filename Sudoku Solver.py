import time

start_time = time.time()

puzzle = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

puzzle2 = [
    [0,0,0,0,8,0,0,7,0],
    [0,5,8,0,3,0,1,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,2,6,0,0,0,0,9,0],
    [4,0,0,0,0,0,0,0,6],
    [7,0,0,0,2,9,3,0,0],
    [0,0,7,0,0,0,9,0,0],
    [1,0,0,2,0,3,0,0,0],
    [0,6,0,0,0,0,0,5,4]
    ]

def solver(puzzle):

    zero_exist = find_zero(puzzle)
    if (zero_exist == False):
        print_puzzle(puzzle)
        return True 
    else:
        row, col = zero_exist

    for i in range(1, 10):
        if (is_safe(puzzle, i, (row,col))):
            puzzle[row][col] = i

            if (solver(puzzle)):
                return True
            puzzle[row][col] = 0
    return False


def is_safe(puzzle, num, pos):

    for i in range(len(puzzle)):
        if(puzzle[pos[0]][i] == num and pos[1] != i):
            return False 
    
    for i in range(len(puzzle)):
        if(puzzle[i][pos[1]] == num and pos[0] != i):
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y *3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x *3 + 3):
            if (puzzle[i][j] == num and (i, j) != pos):
                return False
    return True

def print_puzzle(puzzle):
    for i in puzzle:
        print(i)

def find_zero(puzzle):
    for i, row in enumerate(puzzle):
        for j, column in enumerate(row):
            if(puzzle[i][j] == 0):
                return(i,j)
    return False

solver(puzzle2)
time_to_solve = str(round(time.time() - start_time, 5))
print("Puzzle solved in", time_to_solve , "seconds.")

