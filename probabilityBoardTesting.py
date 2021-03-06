import random

BOARD_SIZE = 10
MIN_SHIP_LENGTH = 3
WATER = "~"
SHOT = "X"


def resetBoard():
    row = []
    for i in range(BOARD_SIZE):
        row.append(WATER)
    board = []
    for i in range(BOARD_SIZE):
        board.append(row[:])
    return board


def resetProbabilityBoard():
    row = []
    for i in range(BOARD_SIZE):
        row.append(0)
    pBoard = []
    for i in range(BOARD_SIZE):
        pBoard.append(row[:])
    return pBoard


def displayBoard(board):
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            print(board[r][c], end=" ")
        print()
    print()


def calculateHorizontal(probabilityBoard, board):
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE-MIN_SHIP_LENGTH+1):
            openSpace = True
            for i in range(MIN_SHIP_LENGTH):
                if board[r][c+i] != WATER:
                    openSpace = False
            if openSpace:
                for i in range(MIN_SHIP_LENGTH):
                    probabilityBoard[r][c+i] += 1
    

def calculateVertical(probabilityBoard, board):
    for r in range(BOARD_SIZE-MIN_SHIP_LENGTH+1):
        for c in range(BOARD_SIZE):
            openSpace = True
            for i in range(MIN_SHIP_LENGTH):
                if board[r+i][c] != WATER:
                    openSpace = False
            if openSpace:
                for i in range(MIN_SHIP_LENGTH):
                    probabilityBoard[r+i][c] += 1


def calculateProbabilities(probabilityBoard, board):
    calculateHorizontal(probabilityBoard, board)
    calculateVertical(probabilityBoard, board)


def fireRandomShotsOnBoard(board, numShots):
    for i in range(numShots):
        randRow = random.randint(0,BOARD_SIZE-1)
        randCol = random.randint(0,BOARD_SIZE-1)
        board[randRow][randCol] = SHOT


def main():
    board = resetBoard()
    fireRandomShotsOnBoard(board, 3)
    probabilityBoard = resetProbabilityBoard()
    calculateProbabilities(probabilityBoard, board)
    displayBoard(board)
    displayBoard(probabilityBoard)


main()
