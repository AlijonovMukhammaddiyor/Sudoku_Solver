from Sudoku import *
import sys


sys.setrecursionlimit(10**4)

def increment(sudoku, changedCells):
    found = False
    x, y, begin = changedCells[-1]
    changedCells.pop()
    sudoku.reset(x, y)
    for j in range(begin+1,10):
        if sudoku.checkValid(j, x, y):
            sudoku.setValue(j, x, y)
            found = True
            changedCells.append((x, y, j))
            #sleep(3)
            
    if not found:
        increment(sudoku, changedCells)
        
        
def solve_it(sudoku, changedCells):
    if sudoku.isBoardFull():
        sudoku.print_board(changedCells)
        return
    
    for y in range(9):
        for x in range(9):
            if sudoku.getValue(x, y) == 0:
                found = False
                for i in range(1, 10):
                    if sudoku.checkValid(i, x, y):
                        sudoku.setValue(i, x, y)
                        found = True
                        changedCells.append((x, y, i))
                        #sudoku.print_board()
                        break
                if not found:
                    increment(sudoku, changedCells)
                    solve_it(sudoku, changedCells)
    if sudoku.isBoardFull():
        sudoku.print_board(changedCells)
        sys.exit(0)

board = [[8,0,0,0,0,0,0,0,0],
         [0,0,3,6,0,0,0,0,0],
         [0,7,0,0,9,0,2,0,0],
         [0,5,0,0,0,7,0,0,0],
         [0,0,0,0,4,5,7,0,0],
         [0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,5,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
sudoku = Sudoku(board)
changedCells = []
solve_it(sudoku, changedCells)
                
