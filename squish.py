import turtle
import random

def drawBoard(wn,t,cols,rows):
    wn.tracer(False)
    for row in range(rows+1):
        t.up()
        t.goto(0,row)
        t.down()
        t.goto(cols,row)
    for col in range(cols+1):
        t.up()
        t.goto(col,0)
        t.down()
        t.goto(col,rows)
        
def drawMe(t,col,row,colr,marker,board):
    t.up()
    t.goto(col,row)
    t.down()
    t.color("black",colr)
    t.begin_fill()
    t.goto(col+1,row)
    t.goto(col+1,row+1)
    t.goto(col,row+1)
    t.goto(col,row)
    board[row][col]=marker
    t.end_fill()
    
def main():
    print("Use arrow keys to move, s to see logical board, q to quit (focus must be on the screen)")
    #set up board parameters
    cols=15
    rows=15
    wn=turtle.Screen()
    bob=turtle.Turtle()
    wn.setworldcoordinates(0-(cols*.1),0-(rows*.1),cols+(cols*.1),rows+(rows*.1))
    bob.color("black","blue")
    bob.hideturtle()
    
    #set up logical board and draw graphical board
    row=[0]*cols
    board=[]
    for i in range(rows):
        board.append(row[:])
    drawBoard(wn,bob,cols,rows)
    
    #position the player randomly
    global myRow
    global myCol
    myRow=random.randint(0,rows-1)
    myCol=random.randint(0,cols-1)
    myMarker=8
    myColor="blue"
    drawMe(bob,myCol,myRow,myColor,myMarker,board)

    #put in the black, moveable blocks
    iterations = (cols*rows)//4
    blockMarker = 2
    while iterations > 0:
        randomRow = random.randrange(0,rows)
        randomCol = random.randrange(0,cols)
        if board[randomRow][randomCol] == 0:
            drawMe(bob,randomCol,randomRow,"black",blockMarker,board)
            iterations -= 1

        
    
    def fwd():
        global myRow
        if myRow<rows-1:
            colSlice = []
            for row in range(rows):
                colSlice.append(board[row][myCol])
            startingIndexOfPlayer = colSlice.index(myMarker)
            colSlice = colSlice[startingIndexOfPlayer:]
            startingIndexOfPlayer = 0
            if colSlice[startingIndexOfPlayer+1] == blockMarker:
                if 0 in colSlice:
                    firstIndexOfSpace = colSlice.index(0)
                    drawMe(bob,myCol,myRow+1,"white",blockMarker,board)
                    drawMe(bob,myCol,myRow+firstIndexOfSpace,"black",blockMarker,board)

                    drawMe(bob,myCol,myRow,"white",0,board)
                    myRow+=1
                    drawMe(bob,myCol,myRow,myColor,myMarker,board)
                    
            else:
                drawMe(bob,myCol,myRow,"white",0,board)
                myRow+=1
                drawMe(bob,myCol,myRow,myColor,myMarker,board)

    def bkwd():
        global myRow
        if myRow>0:
            colSlice = []
            for row in range(rows):
                colSlice.append(board[row][myCol])
            startingIndexOfPlayer = colSlice.index(myMarker)
            colSlice = colSlice[:startingIndexOfPlayer+1]
            startingIndexOfPlayer = len(colSlice)-1
            if colSlice[startingIndexOfPlayer-1] == blockMarker:
                if 0 in colSlice:
                    firstIndexOfSpace = colSlice[::-1].index(0)
                    drawMe(bob,myCol,myRow-1,"white",blockMarker,board)
                    drawMe(bob,myCol,myRow-firstIndexOfSpace,"black",blockMarker,board)

                    drawMe(bob,myCol,myRow,"white",0,board)
                    myRow-=1
                    drawMe(bob,myCol,myRow,myColor,myMarker,board)

            else:
                drawMe(bob,myCol,myRow,"white",0,board)
                myRow-=1
                drawMe(bob,myCol,myRow,myColor,myMarker,board)

    def lft():
        global myCol
        if myCol>0:
            rowSlice = board[myRow]
            startingIndexOfPlayer = rowSlice.index(myMarker)
            rowSlice = rowSlice[:startingIndexOfPlayer+1]
            startingIndexOfPlayer = len(rowSlice)-1
            if rowSlice[startingIndexOfPlayer-1] == blockMarker:
                if 0 in rowSlice:
                    firstIndexOfSpace = rowSlice[::-1].index(0)
                    drawMe(bob,myCol-1,myRow,"white",blockMarker,board)
                    drawMe(bob,myCol-firstIndexOfSpace,myRow,"black",blockMarker,board)

                    drawMe(bob,myCol,myRow,"white",0,board)
                    myCol-=1
                    drawMe(bob,myCol,myRow,myColor,myMarker,board)
            else:
                drawMe(bob,myCol,myRow,"white",0,board)
                myCol-=1
                drawMe(bob,myCol,myRow,myColor,myMarker,board)

    def rght():
        global myCol
        if myCol<cols-1:
            rowSlice = board[myRow]
            startingIndexOfPlayer = rowSlice.index(myMarker)
            rowSlice = rowSlice[startingIndexOfPlayer:]
            startingIndexOfPlayer = 0
            if rowSlice[startingIndexOfPlayer+1] == blockMarker:
                if 0 in rowSlice:
                    firstIndexOfSpace = rowSlice.index(0)
                    drawMe(bob,myCol+1,myRow,"white",blockMarker,board)
                    drawMe(bob,myCol+firstIndexOfSpace,myRow,"black",blockMarker,board)
                    
                    drawMe(bob,myCol,myRow,"white",0,board)
                    myCol+=1
                    drawMe(bob,myCol,myRow,myColor,myMarker,board)
            else:
                drawMe(bob,myCol,myRow,"white",0,board)
                myCol+=1
                drawMe(bob,myCol,myRow,myColor,myMarker,board)

    def quitProg():
        wn.bye()

    def showBoard():
        for row in board[-1::-1]:
            print(row)
        print()
        
    #Declare event handlers for keyboard events (i.e. what function to run for given keyboard event)
    wn.onkeypress(fwd,"Up")
    wn.onkeypress(bkwd,"Down")
    wn.onkeypress(lft,"Left")
    wn.onkeypress(rght,"Right")
    wn.onkeypress(showBoard,"s")
    wn.onkeypress(quitProg,"q")
    
    #Run turtle mainloop where it listens for events
    turtle.listen()
    turtle.mainloop()
    
main()
