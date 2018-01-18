import cs112_f17_week5_linter
from tkinter import *
from sudoku import *
import copy

#########################################################
# Customize these functions
# You will need to write many many helper functions, too.
#########################################################
#By Shivum Agarwal
#shivuma
#Section G


def init(data):
    # load data.xyz as appropriate
    data.rows = 9
    data.columns = 9
    data.boxHeight = data.height/data.rows
    data.boxLength = data.width/data.columns
    data.highlightXCoord = 0
    data.highlightYCoord = 0
    data.Xindex = data.highlightXCoord/data.boxLength
    data.Yindex = data.highlightYCoord/data.boxHeight
    #creates essential varaibles to be used for sudoku creation 

   
    data.permList = []
    for i in range (data.rows):
        for j in range(data.columns):
             if (data.board[i][j] != 0):
                 data.permList.append((i,j))
    #creates list full of values that were already in the sudoku
    
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    if (event.keysym == "Up"):
        data.highlightYCoord -= data.boxHeight
        data.Yindex =  roundHalfUp(data.highlightYCoord/data.boxHeight)
        data.Xindex =  roundHalfUp(data.highlightXCoord/data.boxLength)
        #moves the highlighted space up by decreasing Ycoord of highlight


        if (data.highlightYCoord < 0):
            data.highlightYCoord = data.height-data.boxHeight
        #when highlight is at top, highlight will reappear on the bottom
     
       
   
    
    if (event.keysym == "Down"):
        data.highlightYCoord += data.boxHeight
        data.Yindex =  roundHalfUp(data.highlightYCoord/data.boxHeight)
        data.Xindex =  roundHalfUp(data.highlightXCoord/data.boxLength)
        #moves the highlighted space down by increasing Ycoord of highlight

   
        if (data.highlightYCoord > data.height-data.boxHeight):
            data.highlightYCoord = 0
        #when highlight is at bottom, highlight will reappear on the top



    if (event.keysym == "Right"):
        data.highlightXCoord += data.boxLength
        data.Yindex =  roundHalfUp(data.highlightYCoord/data.boxHeight)
        data.Xindex =  roundHalfUp(data.highlightXCoord/data.boxLength)
        #moves the highlighted space right by increasing Xcoord of highlight


        if (data.highlightXCoord > data.width-data.boxLength):
            data.highlightXCoord = 0
        #resets highlight to leftmost square if it goes outofbounds to the right


    if (event.keysym == "Left"):
        data.highlightXCoord -= data.boxLength
        data.Yindex =  roundHalfUp(data.highlightYCoord/data.boxHeight)
        data.Xindex =  roundHalfUp(data.highlightXCoord/data.boxLength)
        #moves the highlighted space left by decreasing Xcoord of highlight


        if (data.highlightXCoord < 0):
            data.highlightXCoord = data.width-data.boxLength
        #resets highlight to rightmost square if it goes outofbounds to the left



    listofPossibles= ["0","1","2","3","4","5","6","7","8","9"]
    if (event.keysym in listofPossibles):
        addVal(data,event.keysym)
    #accounts for the user input of new values into the sudoku 
        
        
        
    
    pass

def redrawAll(canvas, data):
    # draw in canvas
  
    drawHighlight(data,canvas)
    drawRealGrid(data,canvas)
    #draws the highlight and sudoku 
    
    if (gameOver(canvas,data)):
        canvas.create_rectangle(data.width/4, data.height/4,
        3*data.width/4,3*data.height/4, fill = "gray")
        canvas.create_text(data.width/2,data.height/2,
        text = "You Win! Congrats", fill = "Red", font="Helvetica 26")
    #Creates a win message box after completing the entire sudoku

    pass
    
def gameOver(canvas, data):
  #  print(data.board)
    for i in range (len(data.board)):
     #   print (data.board[i], 0 in data.board[i])
        if (0 in data.board[i]):
            return False 
    return True
    #checks if the sudoku has been completely filled out or not
       

def addVal(data,StringNum):
    val = int (StringNum)
    if (data.board[data.Yindex][data.Xindex] != 0):
        return data.board
    #prevents the editing of a sudoku box if there is already a number 
    else:
        newBoard = copy.deepcopy(data.board)
        newBoard[data.Yindex][data.Xindex] = val
        #creates a copy of sudoku and inputs the val that user inputs
        if (isLegalSudoku(newBoard)):
            data.board = newBoard
            return data.board
        #if the newboard is legal, the original board is returned with new val  
        elif (not isLegalSudoku(newBoard)):
            return data.board
        #doesn't input new number into box if it's illegal


def drawHighlight(data,canvas):
    x =  data.highlightXCoord
    y =  data.highlightYCoord
    #gets coordinate of highlight
    canvas.create_rectangle(x,y,data.boxLength+x,
    data.boxHeight+y,fill = "yellow") 
    #draws the actual highlight
    

def drawRealGrid(data,canvas):
    width = data.width
    height = data.height
    rows = data.rows 
    columns = data.columns
    sudokuboard = data.board
    boxHeight = data.boxHeight
    boxLength = data.boxLength
    #sets local variables for creation of actual grid
    
    canvas.create_line(-1, 4, width, 4, width = 5)
    canvas.create_line(-1, height, width, height, width = 5)
    canvas.create_line(4, 0, 4, height, width = 7)
    canvas.create_line(width, 0, width, height, width = 5)
    #Creates edgelines of grid
        
    for i in range(columns):
        if (i % (columns**0.5) == 0):
            canvas.create_line(i*boxLength, 0, i*boxLength, height, width = 5)
            #creates bolded vertical lines to show sudoku blocks
        else:
            canvas.create_line(i*boxLength, 0, i*boxLength, height)
            #creates normal vartical lines to draw sudoku board 
    for i in range(rows):
        if (i % (rows**0.5) == 0):
            canvas.create_line(0, i*boxHeight, width, i*boxHeight, width = 5)
            #creates bolded horizontal lines to show sudoku blocks
        else:
            canvas.create_line(0, i*boxHeight, width, i*boxHeight)
            #creates normal horizontal lines to draw sudoku board 
    
    for i in range (rows):
        for j in range(columns):
            Xcoord = ((j)*boxHeight+0.5*boxHeight)
            Ycoord = (i*boxLength+0.5*boxLength)
            #gets coordinate of where sudoku values should be placed
            if (sudokuboard[i][j] != 0 and (i,j) in data.permList):
                canvas.create_text(Xcoord,Ycoord,
                text = str(sudokuboard[i][j]),fill = "black", 
                font="Helvetica 26")
                #draws the numbers in black if it was in the initial board
            elif (sudokuboard[i][j] != 0 and (i,j) not in data.permList) :
                canvas.create_text(Xcoord,Ycoord,
                text = str(sudokuboard[i][j]), fill = "blue", 
                 font="Helvetica 26")
                #draws the numbers in blue if it was user inputted

  

########################################
# Do not modify the playSudoku function.
########################################


def playSudoku(sudokuBoard, width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.board = sudokuBoard

    # Initialize any other things you want to store in data
    init(data)

    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()


    # set up events
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))

    # Draw the initial screen
    redrawAll(canvas, data)

    # Start the event loop
    root.mainloop()  # blocks until window is closed
    print("bye!")

def main():
    cs112_f17_week5_linter.lint() # check style rules
    
    board = [
        [1,2,3,4,5,6,7,8,9],
        [5,0,8,1,3,9,6,2,4],
        [4,9,6,8,7,2,1,5,3],
        [9,5,2,3,8,1,4,6,7],
        [6,4,1,2,9,7,8,3,5],
        [3,8,7,5,6,4,0,9,1],
        [7,1,9,6,2,3,5,4,8],
        [8,6,4,9,1,5,3,7,2],
        [2,3,5,7,4,8,9,1,6]
        ]
    playSudoku(board)

if __name__ == '__main__':
    main()
