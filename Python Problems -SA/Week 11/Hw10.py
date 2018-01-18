import types

def getLocalMethods(clss):
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class.
    result = [ ]
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)
    
 
 
 
class Gate(object): 
    def __init__(self):
        self.input1 = None
        self.input2 = None 
        self.numInputs = 2
        
        
    def __str__(object):
        
        message = type(object).__name__
        
        
        return message
        
    def numberOfInputs(self):
        return self.numInputs
    
    def setInputs(self, val, expression):
        if (val == 0):
            if (expression == True):
                self.input1 = True
            else:
                self.input1 = False
                
        elif (val == 1):
            if (expression == True):
                self.input2 = True
            else:
                self.input2 = False
        
    
class AndGate(Gate):
    def getOutput(self):


class OrGate(Gate):
    def getOutput(self):

class NotGate(Gate):
    def getOutput(self):
        
    def numberOfInputs(self):



def testGateClasses():
    print("Testing Gate Classes... ", end="")

    # require methods be written in appropriate classes
    assert(getLocalMethods(Gate) == ['__init__', '__str__',
                                     'numberOfInputs', 'setInput'])
    assert(getLocalMethods(AndGate) == ['getOutput'])
    assert(getLocalMethods(OrGate) == ['getOutput'])
    assert(getLocalMethods(NotGate) == ['getOutput', 'numberOfInputs'])

    # make a simple And gate
    and1 = AndGate()
    assert(type(and1) == AndGate)
    assert(isinstance(and1, Gate) == True)
    assert(and1.numberOfInputs() == 2)
    and1.setInput(0, True)
    and1.setInput(1, False)
    # Hint: to get the name of the class given an object obj,
    # you can do this:  type(obj).__name__
    # You might do this in the Gate.__str__ method...
    assert(str(and1) == "And(True,False)")
    assert(and1.getOutput() == False)
    and1.setInput(1, True) # now both inputs are True
    assert(and1.getOutput() == True)
    assert(str(and1) == "And(True,True)")

    # make a simple Or gate
    or1 = OrGate()
    assert(type(or1) == OrGate)
    assert(isinstance(or1, Gate) == True)
    assert(or1.numberOfInputs() == 2)
    or1.setInput(0, False)
    or1.setInput(1, False)
    assert(or1.getOutput() == False)
    assert(str(or1) == "Or(False,False)")
    or1.setInput(1, True)
    assert(or1.getOutput() == True)
    assert(str(or1) == "Or(False,True)")

    # make a simple Not gate
    not1 = NotGate()
    assert(type(not1) == NotGate)
    assert(isinstance(not1, Gate) == True)
    assert(not1.numberOfInputs() == 1)
    not1.setInput(0, False)
    assert(not1.getOutput() == True)
    assert(str(not1) == "Not(False)")
    not1.setInput(0, True)
    assert(not1.getOutput() == False)
    assert(str(not1) == "Not(True)")

    print("Passed!")

testGateClasses()