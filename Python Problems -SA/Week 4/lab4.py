#################################################
# Lab4
#################################################

import cs112_f17_week4_linter
import math, string, copy

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

#################################################
# Problems
#################################################

def lookAndSay(a):
    
    if (a == []): return []
    
    counter = 0
    b = []
    pastNums = []
    
    for i in range (len(a)):
        if (a[i] not in pastNums):
            counter = a.count(a[i])
            b.append((counter,a[i]))   
            pastNums.append(a[i])
        
  
    return b

    
    
def inverseLookAndSay(a):
    
    b = []
    
    for i in range (len(a)):
        index = a[i]
        count = index[0]
        for i in range (count): 
            b.append(index[1])
    
    return b
    
def splitFunc(puzzle):
    list = puzzle.split("+")
    string1 = list[1]
    list2 = string1.split("=")
    list3 = list1+list2
    
    return list
    

def solvesCryptarithm(puzzle, solution):
    current = "" 
    output = []
    for i in range (len(puzzle)):
        char = puzzle[i]
        if char.isalpha():
            current = current + str(solution.find(char))
        else:
            output.append(current)
            current = "" 
    if int(output[0])+int(output[1]) == int(current):
        return True
    return False

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
import math

def drawStar(canvas, cx, cy, diameter, numPoints, color):
    radius = diameter/2 
    angle = math.radians(90)
    PointList = [] 
    for i in range(numPoints*2):
        if (i%2 ==0):
            x = cx + radius*math.cos(angle)
            y = cy - radius*math.sin(angle)
            PointList.append((x,y))
            angle -= math.radians((360/(numPoints*2)))
        if (i%2 == 1):
            x = cx + (3/8)*radius*math.cos(angle)
            y = cy - (3/8)*radius*math.sin(angle)
            PointList.append((x,y))
            angle -= math.radians((360/(numPoints*2)))
    canvas.create_polygon(PointList, fill = color)


def drawStarHelper(centerX, centerY, diameter, numPoints, color, 
                   winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()

    drawStar(canvas, centerX, centerY, diameter, numPoints, color)
    

    root.mainloop()


def drawUnitedStatesFlag(winWidth=950, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()    
    stripheight = winHeight/13
    
    canvas.create_rectangle(0,0,950,500, fill="white")
    for i in range (0,13,2):
            canvas.create_rectangle(0,stripheight*i,winWidth,stripheight*(i+1), 
            fill="red", width = 0)

    blueHeight = stripheight*7
    blueWidth = winWidth*(.76/1.9)
    
    canvas.create_rectangle(0,0,blueWidth,blueHeight,fill = "blue") 

    coordX = blueWidth/12
    coordY = blueHeight/10
    diameter = 0.0616*winWidth*.5
    i = 0
    
    for i in range (1,10,2):
        for j in range (1,12,2):
            drawStar(canvas, coordX * (j), coordY* (i),diameter,5,"white")
    
    for i in range (2,9,2):
        for j in range (2,11,2):
            drawStar(canvas, coordX * (j), coordY* (i),diameter,5,"white")



    root.mainloop()

def testDrawStar():
    print("Testing drawStar()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawStarHelper(250, 250, 500, 5, "gold")
    drawStarHelper(300, 400, 100, 4, "blue")
    drawStarHelper(300, 200, 300, 9, "red")
    print("Done!")

def testDrawUnitedStatesFlag():
    print("Testing drawUnitedStatesFlag()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    drawUnitedStatesFlag()
    drawUnitedStatesFlag(winWidth=570, winHeight=300)
    print("Done!")

#################################################
# Test Functions
#################################################

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def testSolvesCryptarithm():
    print("Testing solvesCryptarithm()...", end="")
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDRS"))
    # from http://www.cryptarithms.com/default.asp?pg=1
    assert(solvesCryptarithm("NUMBER+NUMBER=PUZZLE", "UMNZP-BLER"))
    assert(solvesCryptarithm("TILES+PUZZLES=PICTURE", "UISPELCZRT"))
    assert(solvesCryptarithm("COCA+COLA=OASIS", "LOS---A-CI"))
    assert(solvesCryptarithm("CROSS+ROADS=DANGER", "-DOSEARGNC"))

    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDR-") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY-ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONY","OMY--ENDRS") == False)
    assert(solvesCryptarithm("SEND+MORE=MONEY","MOY--ENDRS") == False)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testLookAndSay()
    testInverseLookAndSay()
    testSolvesCryptarithm()
    testDrawStar()
    testDrawUnitedStatesFlag()

def main():
    cs112_f17_week4_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
