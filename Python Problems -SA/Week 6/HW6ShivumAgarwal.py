# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import random 

####################################
# customize these functions
####################################
#By Shivum Agarwal
#shivuma
#Section G

def dimensions(data):
    data.Score = 0
    data.ScoreX = 20
    data.ScoreY = data.height-20 
    #sets dimensions for the initial Score and its coords

    data.Time = 20
    data.TimeX = 20
    data.TimeY = 20
    #sets dimensions for the intial Time and its coords


def bounds(data):
    leftX = data.width//2-data.width
    topY = data.height//2-data.height
    rightX = data.width//2+data.width
    bottomY = data.height//2+data.height
    #sets the corners to be used to create boundary
    
    data.leftBound = [leftX,topY,leftX,bottomY,5]
    data.rightBound = [rightX,topY,rightX,bottomY,5]
    data.upBound = [leftX,topY,rightX,topY,5]
    data.downBound = [leftX,bottomY,rightX,bottomY,5]
    data.bounds = [data.leftBound,data.rightBound,data.upBound,data.downBound]
    #sets the coords of the lines that will form the boundary

def firstCircle(data):
    targetLen = 50 
    data.initTarget = [data.width//2,data.height//2,
                            data.width//2+targetLen,data.height//2+targetLen
                            ,targetLen//2]
    data.counter = True

def init(data):
    data.gameWidth = data.width*2
    data.gameHeight = data.height*2 
    #dimensions of game
    data.ListofTargets = []
    #list to contain all the target coords    
  
    dimensions(data)
    bounds(data)
    #incorporates the initial conditions of the dimension and the boundaries
    
    data.GameStart = True
    data.GameOver = False
    #initial game states
    
    data.numCircles = 5
    #num of circles to be created for the target
    
    firstCircle(data)
    #initial conditions of the target on the start screen
    
    pass

def mousePressed(event, data):
    # used to determine whether the user clicked the target correctly
    for i in range (len(data.ListofTargets)-1,-1,-1):
        if (event.x > data.ListofTargets[i][0] and  
            event.x < data.ListofTargets[i][2]): #checks the Xcoord of mouse
            if (event.y > data.ListofTargets[i][1] and 
                event.y < data.ListofTargets[i][3]): #checks Ycoord of mouse
                    data.ListofTargets.remove(data.ListofTargets[i])
                    #makes the target dissapear if user clicks it
                    
                    data.Score +=1
                    if (data.Score % 5 == 0):
                        data.Time += 1
                    #increments the score for each target clicked
                    #time is added for every five targets clicked
    print(event.x,event.y)

def keyPressed(event, data):
    #takes user key inputs to move around the board of game
    if (data.GameStart == False):
        if (event.keysym == "Up"):
            Scroller(data,0,25)
        if (event.keysym == "Down"):
            Scroller(data,0,-25)
        if (event.keysym == "Right"):
            Scroller(data,-25,0)
        if (event.keysym == "Left"):
            Scroller(data,25,0)
    #scrolls through board depending on click direction
    
    elif (data.GameStart == True):
        if (event.keysym == "p"):
            data.GameStart = False
        #starts game if user presses p 
    if (data.GameOver == True):
        if (event.keysym == "s"):
            restart(data)
        #restarts game if user presses s
    
    pass

def Scroller(data, Xincrement, Yincrement):
    #scrolls through the entire game depending on user clicks
   
    for i in range(len(data.ListofTargets)):
        for j in range (len(data.ListofTargets[i])-1):
            if (j % 2 == 0):
                data.ListofTargets[i][j] += Xincrement
            else:
                data.ListofTargets[i][j] += Yincrement
    #moves the coordinates of each target on the screen based on user click
   
    for i in range (len(data.bounds)):
        for j in range (len(data.bounds[i])-1):
            if (j%2 == 0):
                data.bounds[i][j] += Xincrement
            else: 
                data.bounds[i][j] += Yincrement
    #moves the boundaries on the screen based on user click

  

def moveInit(data,increment):
    #moves the initial target in the start screen
    data.timerDelay = 100
    change = 10*increment
    #sets the speed of movement of the start screen target
    
    if (data.timerDelay % 100 == 0):
        for i in range (len(data.initTarget)-1):
                data.initTarget[i] -= change
        #moves the target diagonally 
    if (data.initTarget[1] <=10):
        data.counter = False
        #used to change direction of target if it hits boundary
    if (data.initTarget[3] >= data.height):
        data.counter = True
        #used to change direction of target if it hits boundary

  

def timerFired(data):
    #deals with the rate of intial target speed and rate of target creation
   
    if (data.GameStart == True):
        if (data.initTarget[1] > 10 and data.counter == True):
            moveInit(data, 1)
        #moves the target diagonally north west 
        elif (data.initTarget[1] >= 10 and data.initTarget[3] < data.height 
              and data.counter == False):
            moveInit(data, -1)
        #moves the target diagonally south east 

    elif (data.GameStart == False):
        data.timerDelay = 1000
        #the rate at which targets will appear
        if (data.timerDelay % 100 == 0):
            data.Time -= 1
            newTarget(data)
        #time goes down each second and a new target is generated every second
        if (data.Time == 0):
            data.GameOver = True
        #ends the game when the time becomes 0

    pass
    
def newTarget(data):
    #creates the properties of new target that is to be drawn on board
    
    if (data.GameStart == False and data.GameOver == False):
        targetLen = random.randint(10,50)
        #create the size of target
        
 
        X1 = random.randint(data.leftBound[0],data.rightBound[0]-targetLen)
        Y1 = random.randint(data.upBound[1],data.downBound[1]-targetLen)
        X2 = X1+targetLen
        Y2 = Y1+targetLen
        #gets the coordinates of the randomly generated target
        
        rad = targetLen//2 
        #gets radius
    
        target = [X1,Y1,X2,Y2,rad]
    
        data.ListofTargets.append(target)
        #target is added to big list so that it can be processed in game
        
def drawinitTarget(data,canvas):
    #draws the intial target in the title screen
    canvas.create_oval(data.initTarget[0],data.initTarget[1],
                        data.initTarget[2],data.initTarget[3],fill = "white",
                        outline = "")
    #draws the first circle of the initial target
   
    scale = data.initTarget[4]/data.numCircles
    #gets the amount by which each new circle needs to be drawn
 
    for i in range(data.numCircles):
        if (i % 2 == 0):
            canvas.create_oval(data.initTarget[0]+i*scale,
            data.initTarget[1]+i*scale, data.initTarget[2]-   
            i*scale,data.initTarget[3]-i*scale, fill= "red",outline = "")
            #creates the red inner circles
        elif (i % 2 != 0):
            canvas.create_oval(data.initTarget[0]+i*scale,
            data.initTarget[1]+i*scale, data.initTarget[2]-   
            i*scale,data.initTarget[3]-i*scale, fill= "white",outline = "")
            #creates the white inner circles

def drawTarget(data,canvas):
    #takes target information and draws the actual targets on the canvas
    for i in range(len(data.ListofTargets)):
        target = data.ListofTargets[i] 
        canvas.create_oval(target[0],target[1],target[2],target[3],
        fill = "white",outline = "")
        #creates the first circle of the new target
     
        radius = target[4]
        scale = radius/data.numCircles
        for i in range(data.numCircles):
            if (i % 2 == 0):
                canvas.create_oval(target[0]+i*scale,target[1]+i*scale,
                               target[2]-i*scale,target[3]-i*scale, fill
                               = "red",outline = "")
                #creates the red inner circles
            elif (i % 2 != 0):
                canvas.create_oval(target[0]+i*scale,target[1]+i*scale,
                               target[2]-i*scale,target[3]-i*scale, fill
                               = "white",outline = "")
                #creates the white inner circles
    
def drawGameStart(data,canvas):
    canvas.create_text(data.width/2,data.height/3,text = "Targets Game!!"
                      ,fill = "black", font="Helvetica 26")
    canvas.create_text(data.width/2,2*data.height/3,text = 
                      ("Press P to play! "), 
                      fill = "Black", font="Helvetica 26") 
    #draws the Start screen 
                      

def displayScoreandTime(data,canvas):
    canvas.create_text(data.ScoreX,data.ScoreY, text = str(data.Score),
    fill = "Black", font="Helvetica 16")
    canvas.create_text(data.TimeX,data.TimeY, text = str(data.Time),
    fill = "Black", font="Helvetica 16")
    #displays the score and the time that is regularly updated
    

def drawGameOver(data,canvas):
    score = str(data.Score)
    canvas.create_rectangle(0,0,data.width,data.height,fill = "red")
    canvas.create_text(data.width/2,data.height/3,text = "HAHA TAKE THIS L!!"
                      ,fill = "black", font="Helvetica 26")
    canvas.create_text(data.width/2,1.5*data.height/3,text = 
                      ("Your Final Score is: ", score), 
                      fill = "Black", font="Helvetica 26") 
    canvas.create_text(data.width/2,2*data.height/3,
            text = "Press S to play again!!",fill = "black", font="Helvetica 26")       
    #draws the game over screen according to specifications
    

def drawBound(data,canvas):
    canvas.create_line(data.leftBound[0],data.leftBound[1],data.leftBound[2],
                       data.leftBound[3],width = data.leftBound[4])
    canvas.create_line(data.upBound[0],data.upBound[1],data.upBound[2],
                       data.upBound[3],width = data.upBound[4])
    canvas.create_line(data.downBound[0],data.downBound[1],data.downBound[2],
                       data.downBound[3],width = data.downBound[4])
    canvas.create_line(data.rightBound[0],data.rightBound[1],data.rightBound[2] 
                      ,data.rightBound[3],width = data.rightBound[4])
    #draws the left,right,top, and bottom lines of the board
    
def restart(data):
    if (data.GameOver == True):
        init(data)
    #restarts the entire game if game over

def redrawAll(canvas, data):
    if (data.GameStart == True):
        drawinitTarget(data,canvas)
        drawGameStart(data,canvas)
        #draws the components of the start screen 
    if (data.GameOver == False and data.GameStart == False):
        drawTarget(data,canvas)
        displayScoreandTime(data,canvas)
        drawBound(data,canvas)
        #draws the actual board of the game itself
    # draw in canvas
    elif (data.GameOver == True):
        drawGameOver(data,canvas)
        #draws the game over screen
    pass
    
def testnewTarget(testdata):
    radius = testdata.ListofTargets[0][4]
    print(testdata.ListofTargets)
    print(testdata.width*2)
    assert(radius > 5 and radius < 25)
    assert(testdata.ListofTargets[0][0]> 0 and 
           testdata.ListofTargets[0][2]<testdata.width*2)
    assert(testdata.ListofTargets[0][1]> 0 and 
           testdata.ListofTargets[0][3]<testdata.height*2)
    print("New Target: Passed!")
    
def bounds(testdata):
    leftX = testdata.width//2-testdata.width
    topY = testdata.height//2-testdata.height
    rightX = testdata.width//2+testdata.width
    bottomY = testdata.height//2+testdata.height
    #sets the corners to be used to create boundary
    
    testdata.leftBound = [leftX,topY,leftX,bottomY,5]
    testdata.rightBound = [rightX,topY,rightX,bottomY,5]
    testdata.upBound = [leftX,topY,rightX,topY,5]
    testdata.downBound = [leftX,bottomY,rightX,bottomY,5]
    testdata.bounds = [testdata.leftBound,testdata.rightBound,
                       testdata.upBound,testdata.downBound]
    #sets the coords of the lines that will form the boundary


def testAll():
    #Tests all the functions
    class Struct(object): pass
    testdata = Struct()
    testdata.width = 300
    testdata.height = 300
    testdata.timerDelay = 1000 # milliseconds
    testdata.Score = 0
    testdata.ScoreX = 20
    testdata.ScoreY = testdata.height-20 
    testdata.ListofTargets = []
    #sets dimensions for the initial Score and its coords
    testdata.Time = 20
    testdata.TimeX = 20
    testdata.TimeY = 20
    testdata.GameStart = False
    testdata.GameOver = False
    bounds(testdata)
    newTarget(testdata)

    testnewTarget(testdata)

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

run(400, 400)
testAll()
