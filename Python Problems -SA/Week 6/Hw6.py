# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import random 

####################################
# customize these functions
####################################

def init(data):
    data.gameWidth = 2*data.width 
    data.gameHeight = 2*data.height 
    data.ListofTargets = []
    createTarget(data)


    pass

def mousePressed(event, data):
    # use event.x and event.y
    print(event.x, event.y)
    
    for i in range (len(data.ListofTargets)):
        if (event.x > data.ListofTargets[i][4] and 
            event.x < data.ListofTargets[i][5]):
            if (event.y > data.ListofTargets[i][4] 
                and event.y < data.ListofTargets[i][5]):
                    print("YEETTTT")
                    data.ListofTargets.remove(data.target)
                    
    print(data.ListofTargets)
    
    
    pass

    


def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
 
    pass

def createTarget(data):
    data.targetLen = random.randint(45,50)
    
    data.targetPoint1 = random.randint(0,data.width//2-data.targetLen//2)
    data.targetPoint2 = data.targetPoint1+data.targetLen
    
    print(data.targetPoint1,data.targetPoint2)
    
    data.targetPoint3 = data.targetPoint1+data.targetLen//9
    data.targetPoint4 = data.targetPoint2-data.targetLen//9
    
    data.targetPoint5 = data.targetPoint3+data.targetLen//8
    data.targetPoint6 = data.targetPoint4-data.targetLen//8
    
    data.targetPoint7 = data.targetPoint5+data.targetLen//8
    data.targetPoint8 = data.targetPoint6-data.targetLen//8
    
    data.targetPoint9 = data.targetPoint7+data.targetLen//9
    data.targetPoint10 = data.targetPoint8-data.targetLen//9

    
    data.target = [data.targetPoint1,data.targetPoint2,data.targetPoint3,
                    data.targetPoint4,data.targetPoint5,data.targetPoint6,
                    data.targetPoint7,data.targetPoint8,data.targetPoint9,
                    data.targetPoint10]
   
    data.ListofTargets.append(data.target)


def drawTarget(data,canvas):

    canvas.create_oval(data.target[0],data.target[0],
                       data.target[1],data.target[1],fill = "red")
    canvas.create_oval(data.target[2],data.target[2],
                       data.target[3],data.target[3],fill = "white")
    canvas.create_oval(data.target[4],data.target[4],
                       data.target[5],data.target[5],fill = "red")
    canvas.create_oval(data.target[6],data.target[6],
                       data.target[7],data.target[7],fill = "white")
    canvas.create_oval(data.target[8],data.target[8],
                       data.target[9],data.target[9],fill = "red")
    

    
   




def drawBound(data,canvas):
    canvas.create_line(4,4,4,data.gameHeight,width = 5)

def redrawAll(canvas, data):
    drawBound(data,canvas)
    drawTarget(data,canvas)
    # draw in canvas
    pass

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

run(400, 200)