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
       
    
