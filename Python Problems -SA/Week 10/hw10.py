import cs112_f17_week10_linter
import os
from tkinter import *
import tkinter
import string

#####################
#By Shivum Agarwal
#shivuma
#Section G
#####################

            
def flatten(L):
    
    if (not isinstance(L,list)):
        return L
    #returns the input if not a lst

    else:
        finalList = []
        for element in L:
            if not isinstance(element,list):
                finalList.append(element)
                #adds the element if not a list
                
            else:
                finalList.extend(flatten(element))
                #recursively gets lists within L and adds them 
        return finalList
        

def noError(f):
    def noError(*args):
        try:
            return(f(*args))
            #if no exception is cast, the code will run normally
        except: 
            return(None)
            #nothing will be returned if an error occurs
    return noError



def mapCoords(constraints):
    mappedCoords = dict()
    for i in range (len(constraints)):
        if (i == 0 or i == 12):
            mappedCoords[constraints[i]] = (0,0),(1,1),(2,2),(3,3),(4,4)
            #maps the top-left and bottom-right corner constraints 
        elif(i > 0 and i < 6):
            mappedCoords[constraints[i]] = ((0,i-1),(1,i-1),(2,i-1),
                                            (3,i-1),(4,i-1))
            #maps the top constraints
        elif (i == 6 or i == 18):
            mappedCoords[constraints[i]] = (4,0),(3,1),(2,2),(1,3),(0,4)
            #maps top right and bottom-left corner constraints
        elif(i > 6 and i < 12):
            mappedCoords[constraints[i]] = ((i-7,0),(i-7,1),(i-7,2),
                                            (i-7,3),(i-7,4))
            #maps the right constraints
        elif(i > 12 and i < 18):
            mappedCoords[constraints[i]] = ((0,17-i),(1,17-i),(2,17-i),
                                            (3,17-i),(4,17-i))
            #maps the bottom constraints
        elif(i > 18 and i < 24):
            mappedCoords[constraints[i]] = ((23-i,0),(23-i,1),(23-i,2),
                                            (23-i,3),(23-i,4))
            #maps the left constraints
                                            
    
    return mappedCoords
    
def createboard():
    board = []
    for i in range (5):
        temp = []
        for j in range (5):
            temp.append("0")
        board.append(temp)
    #creates empty 5 by 5 board
    return board


    
def nextTo(current,coord):
    currentx = current[0]
    currenty = current[1] 
    coordx = coord[0]
    coordy = coord[1] 
    #gets the row and col coordinates for the comparison of coordinates
    
    if (coordx == currentx and abs(currenty-coordy) == 1):
        return True
    #same row diff column
    elif (coordy == currenty and abs(currentx-coordx) == 1):
        return True
    #same column diff row
    elif (abs(currenty-coordy) == 1 and abs(currentx-coordx) == 1):
        return True
    #diagonally one unit apart
    return False

    
def isLegalABC(constraints,board,mappedCoords):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] in constraints):
            #checks if the letter is in constraints
                if not (i,j) in mappedCoords[board[i][j]]:
                    return False
                #not legal if the coordinates don't match constraint
    return True
                

def isCompleteABC(board):
    for i in range (len(board)):
        for j in range (len(board[i])):
            if (board[i][j] == "0"):
                return False
            #checks if there are any empty spaces in the board
    return True

  
def solveABC(constraints, aLocation, char = "A",board = None):
    if (board == None):
        board = createboard()
    #creates the empty board for beginning
   
    mappedCoords = mapCoords(constraints)
    board[aLocation[0]][aLocation[1]] = char 
    #creates the mapped constraints to coords and sets the location of A
    
    if (isCompleteABC(board)):
        return board
    #returns the board if it is complete
    else:
        current = aLocation
        prevChar = char
        #gets the most recent letter 
        for row in range (len(board)):
            for col in range (len(board[row])):
                coord = (row,col)
                nextChar = chr(ord(prevChar)+1)
                #gets the next char 
                if (nextTo(current,coord) and board[row][col] == "0"):
                    board[row][col] = nextChar
                    #places the following letter
                    if (isLegalABC(constraints, board, mappedCoords)):
                        solution = solveABC(constraints, coord,
                                            nextChar,board)
                        #recursively brute forces ABC board
                        if (solution != None):
                            return solution
                    board[row][col] = "0"
                    #backtracks board if implemented solution fails
        return None


        
        
######################
def testFlatten():
    print("Testing flatten...", end="")
    L = [1,2,4,[5,6,[5,3,[2,1]]]] 
    assert(flatten(L) == [1,2,4,5,6,5,3,2,1])
    x = [1,2,[3,4]]
    assert(flatten(x) == [1,2,3,4])
    z = 3 
    assert(flatten(z) == 3)
    
    print("passed")
    
def testNoErrorDecorator():
    print("Testing @noError decorator...", end="")
    @noError
    def f(x, y): return x/y
    assert(f(1, 5) == 1/5)
    assert(f(1, 0) == None)

    @noError
    def g(): return 1/0
    assert(g() == None)

    @noError
    def h(n):
        if (n == 0): return 1
        else: return h(n+1)
    assert(h(0) == 1)
    assert(h(-1) == 1)
    assert(h(1) == None)

    print("Passed!")

def testisLegalABC():
    print('Testing isLegalABC()...', end='')
    mappedCoords = mapCoords("CHJXBOVLFNURGPEKWTSQDYMI")
    board = [['J', 'J', 'K', 'L', 'A'],
                ['H', 'G', 'F', 'A', 'M'],
                ['T', 'Y', 'C', 'E', 'N'],
                ['U', 'S', 'X', 'D', 'O'],
                ['V', 'W', 'R', 'D', 'P']
               ]
    assert(isLegalABC("CHJXBOVLFNURGPEKWTSQDYMI", board, 
                      mappedCoords) == False)
    print('Passed!')

def testisCompleteBoard():
    print('Testing isCompleteBoard()...', end='')
    board = [['J', 'J', 'K', 'L', 'A'],
                ['0', 'G', 'F', 'A', 'M'],
                ['0', 'Y', 'C', 'E', 'N'],
                ['U', 'S', 'X', 'D', 'O'],
                ['V', 'W', 'R', 'D', 'P']
               ]
    assert(isCompleteABC(board) == False)
    print('Passed!')

def testSolveABC():
    print('Testing solveABC()...', end='')
    constraints = "CHJXBOVLFNURGPEKWTSQDYMI"
    aLocation = (0,4)
    board = solveABC(constraints, aLocation)
    solution = [['I', 'J', 'K', 'L', 'A'],
                ['H', 'G', 'F', 'B', 'M'],
                ['T', 'Y', 'C', 'E', 'N'],
                ['U', 'S', 'X', 'D', 'O'],
                ['V', 'W', 'R', 'Q', 'P']
               ]
    assert(board == solution)
    print('Passed!')

######################

def init(data):
    data.level = 0
    
    pass

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if (event.keysym in ["Up", "Right"]):
        data.level += 1
    elif ((event.keysym in ["Down", "Left"]) and (data.level > 0)):
        data.level -= 1
    #changes the recursion level
        
def timerFired(data):
    pass
    
def drawH(canvas, xc, yc, r):
    canvas.create_line(xc-r, yc-r, xc+r, yc-r,width = 4)
    canvas.create_line(xc-r, yc-2*r, xc-r, yc,width = 4)
    canvas.create_line(xc+r, yc-2*r, xc+r, yc,width = 4)
    #draws the actual H on the canvas

    
def fractalH(canvas, xc, yc, r, level):
    if (level == 0):
        drawH(canvas,xc,yc,r)
    #draws the initial H base case
    else:
       
        fractalH(canvas, xc, yc, r, level-1)
        fractalH(canvas, xc+r, yc-3/2*r, r//2, level-1)
        fractalH(canvas, xc-r, yc-3/2*r, r//2, level-1)
        fractalH(canvas, xc+r, yc+r-1/2*r, r//2, level-1)
        fractalH(canvas, xc-r, yc+r-1/2*r, r//2, level-1)

    #recursively draws the next teddy faces for each level    
    

def redrawAll(canvas, data):
    fractalH(canvas, data.width//2, data.height//1.5, 100, data.level)
    canvas.create_text(250, 25,
                       text = "Level %d H-Fractals" % (data.level+1),
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

def testAll():
    testNoErrorDecorator()
    testSolveABC()
    testisLegalABC()
    testisCompleteBoard()
    testFlatten()

def main():
    cs112_f17_week10_linter.lint() # check style rules
    testAll()
    run(600,600)

if __name__ == '__main__':
    main()  