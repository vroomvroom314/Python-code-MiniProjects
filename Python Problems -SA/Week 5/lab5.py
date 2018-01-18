#################################################
# Lab5
#################################################


import cs112_f17_week5_linter


#################################################
# Problems
#By Shivum Agarwal
#Section G
#Collab with Andrew Ye and Ashwath Vijaykumar

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

        
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
    
    


#################################################

def checkLegalBoard(board):
    #checks if the board is properly created 
    
    rows = len(board)
    cols = len(board[0])
    #gets total rows and columns
    
    prevVals = []
    #ensures that only one instance of each element in board
    for i in range (rows):
        for j in range (cols): 
            if (not isinstance(board[i][j], int)):
                return False
            #board is not valid if there are non int elements
            elif (board[i][j] < 1 or board[i][j] > (rows*cols)):
                return False
            #0 or neg vals and values bigger than rows*cols are not legal
            elif (board[i][j] in prevVals):
                return False
            #boards with duplicates are illegal
            elif (not board[i][j] in prevVals):
                prevVals.append(board[i][j])
            #adds new elements to prevVals to prevent duplicates
            elif (1 not in prevVals):
                return False
            #not legal if 1 is not in board
    return True
        

def find2dIndex(num, board):
    #used to find indexes for kings road    
    rows = len(board)
    for i in range (rows):
        if (num in board[i]):
            return (i, board[i].index(num))
            #returns position of num and index i


def isKingsTour(board):
    if (not checkLegalBoard(board)):
        return False
    #automatically not kings tour if board doesn't work
    rows = len(board)
    columns = rows
   
    for i in range(rows * columns):
        #loops through total indexes within boards
        if (i+1 != (rows * columns)):
            firstindex = find2dIndex(i+1, board)
            secondindex = find2dIndex(i+2, board)
            #gets two positions of vals to check their distance
            if (abs(firstindex[0] - secondindex[0]) > 1 or 
                abs(firstindex[1] - secondindex[1]) > 1):
                return False
            #if distance is greeater than 1, kings road is false
  
    return True

    
    
def testIsKingsTour():
    print("Testing isKingsTour()...", end="")
    assert(isKingsTour([[3,2,1],[6,4,9],[5,7,8]]) == True)
    assert(isKingsTour([[1,2,3],[7,4,8],[6,5,9]]) == False)
    assert(isKingsTour([[3,2,1],[6,4,0],[5,7,8]]) == False)
    assert(isKingsTour([[4,3,2],[7,5,10],[6,8,9]]) == False)
    assert(isKingsTour([[1,14,15,16],[13,2,7,6],
                        [12,8,3,5],[11,10,9,4]]) == True)
    print("Passed. ")

def testisLegalSoduku():
    print("Testing isLegalSudoku()...", end="")
    assert(isLegalSudoku([[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
                    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
                    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
                    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
                    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
                    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
                    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
                    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
                    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]))
    assert(isLegalSudoku([[ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
                    [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
                    [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
                    [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
                    [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
                    [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
                    [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
                    [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
                    [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]))
    print("Passed. ")

def main():
    cs112_f17_week5_linter.lint() # check style rules
    testIsKingsTour()
    testisLegalSoduku()
    
if __name__ == '__main__':
    main()