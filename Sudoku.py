from termcolor import cprint

class Sudoku(object):
    def __init__(self,  board):
        self.board = board[:]
        self.width = 9
        self.height = 9
        self.notChanged = self.__isChanged(board)
        #print(self.notChanged)

    def print_board(self, cellsInColor):
        for i in range(self.height):
            for j in range(self.width):
# =============================================================================
#                 if self.board[i][j] == 0:
#                     print("_", end=' ')
# =============================================================================
                if  (j, i) in self.notChanged:
                    cprint(self.board[i][j], 'red', end=" ")
                else:
                    cprint(self.board[i][j], 'blue', end=" ")
                if (j+1)%3 ==0:
                    print("|", end='')
            print()
            if (i+1)%3 == 0:
                print("-"*21)

    def checkValid(self, i, x, y):
        if i in self.board[y]:
            return False
        for j in range(self.height):
            if i == self.board[j][x]:
                return False
        if not self.checkSquare(x, y, i):
            return False
        return True

    def setValue(self, i, x, y):
        self.board[y][x] = i

    def getValue(self, x, y):
        return self.board[y][x]

    def getBoard(self):
        return self.board[:]
    
    def isBoardFull(self):
        for i in self.board:
            if 0 in i:
                return False
        return True
    
    def reset(self, x, y):
        self.board[y][x] = 0
        
    def checkSquare(self, x, y, value):
        xBegin = (x//3) * 3
        yBegin = (y//3) * 3
        for i in range(yBegin, yBegin + 3):
            for j in range(xBegin, xBegin + 3):
                if i!=y and j!=x:
                    if self.board[i][j] == value:
                        return False
        return True
    
    def __isChanged(self,board):
        Notchanged = []
        for i in range(9):
            for j in range(9):
                if board[i][j] > 0:
                    Notchanged.append((j,i))
        return Notchanged
