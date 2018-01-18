import cs112_f17_week10_linter
import os
from tkinter import *
import tkinter




#####################
#By Shivum Agarwal
#Section G
#Collab with Andrew Ye and Ashwath Vijaykumar

#####################
def findLargestFile(path):
    highestTup = largestFile(path)
    return highestTup[1]
    #gets the largest size and gets the path
    
    
def largestFile(path, highSize = 0, bestPath = ""):
    removeDsStore("sampleFiles")
    if (not os.path.isdir(path)):
        #hits a file
        fileSize = os.path.getsize(path)
        #gets the size of a specific file
        if (fileSize > highSize):
            highSize = fileSize
            bestPath = path
        #finds the biggest file and the path that leads to it
    else:
        #hits a folder
        files = os.listdir(path)
        for i in files:
            highSize, bestPath = largestFile(path+"/" + i,
                                highSize, bestPath)
            #recursively goes through folders until it hits a file
    return highSize, bestPath
    #returns the biggest file and the path

def removeDsStore(path):
    if (os.path.isdir(path) == False):
        if (path.endswith(".DS_Store")):
            os.remove(path)
            #gets rid of path that has DS Store
    else:
        for file in os.listdir(path):
            removeDsStore(path + "/" + file)
        #recurisvely goes through folders and updates path



    pass 

#####################
#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

### Your lab5 functions below ###

def areLegalValues(values):
#finds whether or not values given are legal for soduku
    prevVals =[] 
        #used to check if duplicates in values appear
    
    for i in range (len(values)):
        if (values[i] != 0 and values[i] not in prevVals):
            prevVals.append(values[i])
            #adds each digit in values if it hasn't appeared yet
        elif (values[i] == 0):
            continue 
            #skips 0s 
        else:
            return False
            #if a digit appears more than once in values, it's not legal
  
    return True

def isLegalRow(board, row): 
    newRow = board[row]
    #gets row 
    
    Legality = areLegalValues(newRow)
    #checks if the row has legal values
    
    return Legality

def isLegalCol(board, columns):
    
    FinalColumn = []
    for i in range(len(board)):
        FinalColumn += [board[i][columns]]
        #gets column 

   
    Legality = areLegalValues(FinalColumn)
    #checks if the column has legal values

    return Legality

    
def isLegalBlock(board, block):
    
    
    Block = []
    #list to store specific block of board
    
    n = roundHalfUp(len(board)**0.5)
    #gets the block length given the length of board
    X = block // n        
    #gets the X coord of specific block given var block
    Y = block %  n
    #gets the Y coord of specific block given var block

    
    for row in range(X*n,(X+1)*n):
        for col in range(Y*n,(Y+1)*n):
            Block.append(board[row][col])
        #loops through given block of board and adds it to list
    Legality = areLegalValues(Block)
    #checks if the block has legal values
    
    return Legality

    
def isLegalSudoku(board):
    for i in range (len(board)):
        #loops through each count of row, block, and column
        if (not isLegalBlock(board,i) or not isLegalCol(board,i)
            or not isLegalRow(board,i)):
                return False
            #checks if given index of row, column and block is legal
            # if a single one is not legal, returns False
    return True
    
def solveSudoku(board):
    if (isLegalSudoku(board) and noZeroes(board)): 
        return board
    #base case, board is complete
    
    else:
        for row in range (len(board)):
            for col in range (len(board[row])):
                if (board[row][col] == 0):
                    #gets an empty place on board
                    for num in range(1,10):
                        board[row][col] = num
                        #inserts a number into the board space
                        if (isLegalSudoku(board)):
                            solution = solveSudoku(board)
                            #recursively brute forces through sudoku 
                            if (solution != None):
                                return solution
                        board[row][col] = 0
                        #backtracks board if implemented solution fails
                    return None
                        
      

def noZeroes(board):
    for i in range (len(board)):
        if (0 in board[i]):
            return False 
    return True
    #checks for 0s in the entire board
                
######################
#Ignore rest

def testSolveSudoku():
    print('Testing solveSudoku()...', end='')
    board = [
              [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
              [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
              [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
              [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
              [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
              [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
              [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
              [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
              [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
            ]
    solved = solveSudoku(board)
    solution = [
                [5, 3, 4, 6, 7, 8, 9, 1, 2], 
                [6, 7, 2, 1, 9, 5, 3, 4, 8], 
                [1, 9, 8, 3, 4, 2, 5, 6, 7], 
                [8, 5, 9, 7, 6, 1, 4, 2, 3], 
                [4, 2, 6, 8, 5, 3, 7, 9, 1], 
                [7, 1, 3, 9, 2, 4, 8, 5, 6], 
                [9, 6, 1, 5, 3, 7, 2, 8, 4], 
                [2, 8, 7, 4, 1, 9, 6, 3, 5], 
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
               ]
    assert(solved == solution)
    print('Passed!')

def testSolveFile():
    assert(findLargestFile("sampleFiles/folderA") ==
                       "sampleFiles/folderA/folderC/giftwrap.txt")
    assert(findLargestFile("sampleFiles/folderB") ==
                       "sampleFiles/folderB/folderH/driving.txt")
    assert(findLargestFile("sampleFiles/folderB/folderF") == "")
    print('Passed!')





######################

def init(data):
    data.level = 1
    
    pass

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if (event.keysym in ["Up", "Right"]):
        data.level += 1
    elif ((event.keysym in ["Down", "Left"]) and (data.level > 0)):
        data.level -= 1
        
        
def timerFired(data):
    pass
    
def teddyFace(canvas, xc, yc, r):
    canvas.create_oval(xc-r,yc-r,xc+r,yc+r, fill = "brown", width = r/25) 
    canvas.create_oval(xc-r/1.5,yc-r/1.5, xc-r/4, yc-r/4, fill = "black", 
                        width = r/25)
    canvas.create_oval(xc+r/1.5,yc-r/1.5, xc+r/4, yc-r/4, fill = "black", 
                        width = r/25)
    canvas.create_oval(xc-r/2,yc-r/4, xc+r/2, yc+3*r/4, fill = "tan", 
                        width = r/25)
    canvas.create_oval(xc-r/8,yc-r/8, xc+r/8,yc+r/8, fill = "black", 
                        width = r/25)
    #creates the facial features of the teddy like snout, nose, face 

    mouthx1 = xc - r * 1/8
    mouthx2 = xc + r * 1/8  
    mouthy =  yc + r * 1/2
    mouthr = r * 1/16
    canvas.create_arc(mouthx1+2*mouthr, mouthy+2*mouthr, mouthx1-2*mouthr,
                      mouthy-2*mouthr, style = tkinter.ARC, fill = "blue", 
                      start = 270, width = r*0.0375)
    canvas.create_arc(mouthx1+2*mouthr, mouthy+2*mouthr, mouthx1-2*mouthr,
                      mouthy-2*mouthr, style = tkinter.ARC, fill = "blue", 
                      start = 180,width = r*0.0375)
    canvas.create_arc(mouthx2+2*mouthr, mouthy+2*mouthr, mouthx2-2*mouthr,
                      mouthy-2*mouthr, style = tkinter.ARC, fill = "blue", 
                      start = 180,width = r*0.0375)
    canvas.create_arc(mouthx2+2*mouthr, mouthy+2*mouthr, mouthx2-2*mouthr,
                      mouthy-2*mouthr, style = tkinter.ARC, fill = "blue", 
                      start = 270,width = r*0.0375)
    #creates the mouth using 4 arcs 
   
    
def fractalTeddy(canvas, xc, yc, r, level):
    if (level == 0):
        teddyFace(canvas,xc,yc,r)
    #draws the initial teddy base case
    else:
       
        fractalTeddy(canvas, xc, yc, r, level-1)
        fractalTeddy(canvas, xc+r*1.3, yc-r//2*1.5, r//2, level-1)
        fractalTeddy(canvas, xc-r*1.3, yc-r//2*1.5, r//2, level-1)
    #recursively draws the next teddy faces for each level    
    

def redrawAll(canvas, data):
    fractalTeddy(canvas, data.width//2, data.height//1.5, 100, data.level)
    canvas.create_text(250, 25,
                       text = "Level %d Fractal Bear" % (data.level),
                       font = "Arial 26 bold")
    canvas.create_text(250, 50,
                       text = "Use arrows to change level",
                       font = "Arial 10")
    #draws all the actual features and incorporates text on the top of window
    pass

####################################
# use the run function as-is
####################################

def run(width=600, height=600):
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
    data.timerDelay = 100 # milliseconds
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

