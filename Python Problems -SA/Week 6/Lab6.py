# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import random


####################################
# customize these functions
####################################
#By Shivum Agarwal
#Section G
#Collab with Andrew Ye and Ashwath Vijaykumar

def playTetris(data):
    data.rows = 15
    data.cols = 10
    data.cellSize = 20
    data.margin = 30
    #Initialize basic features of board
    data.width = (data.cols*data.cellSize) + 2*data.margin
    data.height = (data.rows*data.cellSize) + 2*data.margin
    #width and height of board are initialized
    data.emptyColor = "blue"
    data.board = []
    drawGrid(data)
    data.Score = 0
    #sets up board 
    
    
def getPieces(data):
    iPiece = [[True,  True,  True,  True]]
    jPiece = [[True, False, False ],
            [True,  True,  True ]]
    lPiece = [[ False, False,  True ],
              [ True,  True,  True ]]
    oPiece = [[  True,  True ],
              [  True,  True ]]
    sPiece = [[ False,  True,  True ],
              [ True,  True, False ]]
    tPiece = [[ False,  True, False ],
              [ True,  True,  True ]]
    zPiece = [[  True,  True, False ],
              [ False,  True,  True ]]
    #sets up piece types for tetris 
    tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
    tetrisPieceColors = [ "red", "yellow", "magenta", "pink", 
                        "cyan", "green","orange" ]
    data.tetrisPieces = tetrisPieces
    data.tetrisPieceColors = tetrisPieceColors
    #puts the pieces and colors in lists 

def init(data):
    # load data.xyz as appropriate
    playTetris(data)
    getPieces(data)
    newFallingPiece(data)
    #loads the entire board
    pass

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if (not GameOver(data)):
        if (event.keysym == "Up"):
            rotatePiece(data)
        #rotates the piece
        if (event.keysym == "Down"):
            moveFallingPiece(data,1,0)
        if (event.keysym == "Left"):
            moveFallingPiece(data,0,-1)
        if (event.keysym == "Right"):
            moveFallingPiece(data,0,1)
    #moves the pieces
    if (event.keysym == "p"):
        ReStart(data)
    #restarts game when game is over
        
    pass
   
def fallingPieceisLegal(data):
    for i in range (len(data.board)):
        for j in range (len(data.board[i])):
            if ([i,j] in data.finalCoord):
                #checks if the coord of the board is in the newblock coords
                if (data.board[i][j] != data.emptyColor):
                    placeFallingPiece(data)
                    #places the piece if it's touching another block
                    return False
        
    for i in range (len(data.finalCoord)):
        pieceRow = data.finalCoord[i][0]
        pieceCol = data.finalCoord[i][1]
        #gets specific coordinate of a point of the falling piece
        if (pieceRow > data.rows-1 or pieceRow < 0):
            placeFallingPiece(data)
            #makes sure that the falling block doesn't escape boundaries
            return False
            #checks the vertical location of the block 
            #places the falling block
        elif (pieceCol>data.cols-1 or pieceCol<0):
            return False
            #checks the horizontal location of the block

    return True
    
def placeFallingPiece(data):
    for i in range (len(data.finalCoord)):
        Index1 = data.finalCoord[i][0]-1
        Index2 = data.finalCoord[i][1]
        #gets the indexes that are to be implemented onto the new board
        if (Index1 < data.rows and Index2 < data.cols):
            data.board[Index1][Index2] = data.fallingPieceColor
            #sets the board with the new piece 
    newFallingPiece(data)
    #creates new fallingPiece
   
    for i in range (len(data.board)):
        if (fullRow(data,data.board[i])):
            #checks if a given row in the board is full
            temp = createNewRow(data)
            #creates a new row of empty space 
            data.board.insert(1,temp)
            #inserts new row 
            data.board.remove(data.board[i+1])
            #removes the row with full row of nonempty squares
            data.Score += 1
            #adds to score for each row deleted
            

def createNewRow(data):
    temp = [] 
    for i in range(data.cols):
        temp.append(data.emptyColor)
    #creates new empty rows
    return temp
            
            
               
def timerFired(data):
    moveFallingPiece(data,1,0)
    #moves the falling piece down one space for each given time interval
    pass

def moveFallingPiece(data,drow,dcol):
    if (not GameOver(data)):
        data.fallingPieceRow += drow
        data.fallingCol += dcol
        #changes the coordinates of given piece
        Coords = []
        finalCoord = []
        #lists used to find full list of coords for given shape
        for i in range (len(data.fallingPiece)):
            for j in range (len(data.fallingPiece[i])):
                if (data.fallingPiece[i][j] == True ):
                    Coords.append([i,j])
        #gets the initial coords of where the shape boolean vals are true
        for i in range (len(Coords)):
            finalCoord.append([Coords[i][0]+data.fallingPieceRow,
                Coords[i][1]+data.fallingCol])
        #gets the final coordinates of the falling shape

        data.finalCoord = finalCoord 
        if(fallingPieceisLegal(data) == False):
            data.fallingPieceRow -= drow
            data.fallingCol -= dcol
            #falling piece can't move if there's a boundary or other blocks 
        

def fullRow(data, board):
    for i in range (len(board)):
        if (board[i] == data.emptyColor):
            return False
    #checks if the given row is completely full with non-empty squares
    return True
    
def displayScore(canvas,data):
    canvas.create_text(10,10, text = str(data.Score),
    fill = "Black", font="Helvetica 16")
    #displays the given score
    
        
def rotatePiece(data):
    fallingPiece = data.fallingPiece
    fallingPieceRow = data.fallingPieceRow
    fallingPieceCol = data.fallingCol
    fallingPieceRows = len(fallingPiece)
    fallingPieceCols = len(fallingPiece[0])
    #initializes local variables to prevent global var changes or errors
    centerRow = fallingPieceRow + fallingPieceRows//2 
    centerCol = fallingPieceCol + fallingPieceCols//2
    #gets center of roation
    newPiece = []
    #new piece will be stored in this list
    for i in range(fallingPieceCols):
        reverse = fallingPieceCols - i - 1
        #gets new column location
        temp = []
        for j in range (fallingPieceRows):
            temp.append(fallingPiece[j][reverse])
            #stores the new column coords in temporary list
        newPiece.append(temp)
        #stores all new columns in big list
    rows = len(newPiece)
    cols = len(newPiece[0])
    #gets  rows and columns for the rotated piece
    newRow = centerRow - rows//2
    newCol = centerCol - cols//2
    #sets new row and column of rotated piece
    data.fallingPieceRow = newRow
    data.fallingCol = newCol
    data.fallingPiece = newPiece
    #initializes the new piece to global vars for falling pieces

  
        
def newFallingPiece (data):
    randomIndex = random.randint(0, len(data.tetrisPieces) - 1)
    randomIndex2 = random.randint(0, len(data.tetrisPieces) - 1)
    #gets random numbers that will be index for falling piece and its color
    data.fallingPiece = data.tetrisPieces[randomIndex]
    data.fallingPieceColor = data.tetrisPieceColors[randomIndex2]
    #creates new falling piece with a shape and a color
    data.fallingPieceRow = 1 
    #row where falling piece is initialized
    fallingCols = len(data.fallingPiece[0])
    data.fallingCol = data.cols//2 - fallingCols//2
    #column where falling piece is initialized
    data.finalCoord = []
    #list where the coords of the given shape will be stored
        
def drawFallingPiece (canvas,data):
    for i in range (len(data.fallingPiece)):
        for j in range (len(data.fallingPiece[0])):
            #loops through entire list of falling piece
            if (data.fallingPiece[i][j] == True):
                drawCell(canvas,data,i+data.fallingPieceRow,
                j+data.fallingCol,data.fallingPieceColor)
                #draws the piece at each location where value is true
        
    

def drawCell(canvas, data, row, col,color):
    Xo = data.margin + (col * data.cellSize)
    X1 = data.margin + ((col + 1) * data.cellSize)
    Yo = data.margin + (row * data.cellSize)
    Y1 = data.margin + ((row + 1) * data.cellSize)
    canvas.create_rectangle(Xo, Yo, X1, Y1, fill = color, 
                            width = 5)
    #gets coordinates of initial and ending points of a rectangle and draws them

def drawGrid(data):
    for i in range(data.rows):
        temp = []
        for j in range(data.cols):
            temp.append(data.emptyColor)
        data.board.append(temp)
    #creates the intial grid with all empty color values
    data.board[0][0] = "red"
    data.board[0][data.cols-1] = "white"
    data.board[data.rows-1][0] = "green"
    data.board[data.rows-1][data.cols-1] = "gray"
    #changes the four corners according to specifications

def drawBoard(canvas,data):
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(canvas, data, row, col,data.board[row][col])
    #draws the entire board based on values of the given board

def drawGameOver(canvas,data):        
    if (GameOver(data)):
        canvas.create_rectangle(0, 0,
        data.width,data.height, fill = "gray")
        canvas.create_text(data.width/2,data.height/3,
        text = "HAHA TAKE THIS L!!", fill = "Red", font="Helvetica 26")
        canvas.create_text(data.width/2,1.5*data.height/3,
        text = ("Your Score is: ", str(data.Score)) , fill = "Red", 
        font="Helvetica 26") 
        canvas.create_text(data.width/2,2*data.height/3,
        text = "Press P to restart", fill = "Red", font="Helvetica 26")
    #draws the gameOver function after the game ends
        


def GameOver(data):
    if (data.board[0][5] != data.emptyColor):
            return True
    return False
    #ensures that the game ends any time the stack of blocks become too high
    

def ReStart(data):
    if (GameOver(data)):
        init(data)
    #restarts the entire game 
        
def redrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "orange")
    drawBoard(canvas,data)
    if (not GameOver(data)):
        drawFallingPiece(canvas,data)
        displayScore(canvas,data)
    drawGameOver(canvas,data)
    #constantly draws the game at every instance after every move
    # draw in canvas
    
    pass



def testMoveFallingPiece(testData):
    print("Testing moveFallingPiece...", end = " ")
    moveFallingPiece(testData, 1, 0)
    assert(testData.fallingPieceRow == 1)
    
    moveFallingPiece(testData,0,-1)
    assert(testData.fallingCol == 3)
    
    
    print("Passed!")
    
def testRotateFallingPiece(testData):
    print("Testing rotateFallingPiece...", end = " ")
    jPiece = [
        [True, False, False],
        [True, True, True]
    ]
    testData.fallingPiece = jPiece
   
    rotation1 = [
        [False, True],
        [False, True],
        [True, True]
    ]
    
    
    rotation2 = [
        [True, True, True],
        [False, False, True]
    ]
    
 
   
    rotatePiece(testData)
    assert(testData.fallingPiece == rotation1)
    rotatePiece(testData)
    assert(testData.fallingPiece == rotation2)
  
    

    print("Passed!")
    

def testAll():
    #Tests all the functions
    class Struct(object): pass
    testData = Struct()
    testData.rows = 15
    testData.cols = 10
    testData.board = []
    testData.emptyColor = "blue"
    testData.finalCoord = []
    for i in range(testData.rows):
        temp = []
        for j in range(testData.cols):
            temp.append(testData.emptyColor)
        testData.board.append(temp)
    jPiece = [
        [True, False, False],
        [True, True, True]
    ]
    testData.fallingPiece = jPiece
    testData.fallingPieceRow = 0
    fallingPieceCols = len(jPiece[0])
    testData.fallingCol = testData.cols//2 - fallingPieceCols//2
    testData.isGameOver = False
    testData.score = 0

    testMoveFallingPiece(testData)
    init(testData)
    testRotateFallingPiece(testData)
    init(testData)



####################################
# use the run function as-is
####################################


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 1000 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

testAll()
run(300, 500)