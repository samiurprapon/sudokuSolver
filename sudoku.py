import numpy as np

grid = np.array([
        [5, 3, 0, 0, 7, 0, 0, 0, 0], 
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0], 
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

def posible(column_index, row_index, value):
    global grid

    for i in range(0, 9):
        if grid[column_index][i] == value:
            return False;
    for i in range(0, 9):
        if grid[i][row_index] == value:
            return False;
    
    x0 = (row_index//3) * 3;
    y0 = (column_index//3) * 3;

    for i in range (0, 3):
        for j in range(0, 3):
            if grid[y0+i][x0+j] == value :
                return False;
    return True;

def solve():
    global grid

    for column_index in range (9):
        for row_index in range (9):
            if grid[column_index][row_index] == 0:
                for value in range (1, 10):
                    if posible(column_index, row_index, value):
                        grid[column_index][row_index] = value
                        solve()
                        grid[column_index][row_index] = 0
                return
    
    print(np.matrix(grid))
    
# print(np.matrix(grid))
solve()

