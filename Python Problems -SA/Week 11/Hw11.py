import types
import cs112_f17_week11_linter


###################

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
    
 
################## 
#By Shivum Agarwal
#Section G
#shivuma
 
 
 
class Gate(object): 
    def __init__(self):
        self.input1 = None
        self.input2 = None 
        self.numInputs = 2
        #superclass variables that are initialized
    
        
    def __str__(object):
        name = type(object).__name__ 
        
        if (name == "AndGate"):
            return "And(" + str(object.input1) +"," + str(object.input2) \
                    + ")"
        #returns above message given that object is AndGate
                    
        if (name == "OrGate"):
            return "Or(" + str(object.input1) +"," + str(object.input2) \
                    + ")"
        #returns above message given that object is OrGate

                    
        if (name == "NotGate"):
            return "Not(" + str(object.input1) + ")"
        #returns above message given that object is NotGate
        
        return name
        
    def numberOfInputs(self):
        return self.numInputs
        #returns number of inputs for And/Or Gate
        
    
    def setInput(self, val, expression):
        if (val == 0):
            if (expression == True):
                self.input1 = True
            else:
                self.input1 = False
        #sets the first input 
            
        elif (val == 1):
            if (expression == True):
                self.input2 = True
            else:
                self.input2 = False
        #sets the second input
    
class AndGate(Gate):
#gate subclass
    
    def getOutput(self):
        return self.input1 and self.input2
        #returns boolean value of inputs with and
    

class OrGate(Gate):
#gate subclass
    def getOutput(self):
        return self.input1 or self.input2
        #returns boolean value of inputs with or


class NotGate(Gate):
#gate subclass

    def getOutput(self):
        return not self.input1
        #returns opposite boolean val of input 
        
    def numberOfInputs(self):     
        return self.numInputs -1 
        #one less input than And/Or classes is returned

###############
class ComplexNumber(object):
    zero = None
    
    def __init__(self, *args):
        if (len(args) == 0):
            self.firstVal = 0
            self.secondVal = 0
        #Complex number is 0+0i if no arguments are given
        elif (len(args) == 1):
            self.firstVal = args[0]            
            self.secondVal = 0
        #Real num is initialized, imaginary num is 0
        elif (len(args) == 2):
            self.firstVal = args[0]
            self.secondVal = args[1]
        #Both real and imaginary numbers are initialized
    
    def __hash__(self):
        return hash(self.firstVal)
        #gets hash value of the real number 
    
    def __eq__(self, other):
        if (str(self) == str(other)):
            return True
        #checks if the returned Strings are the same 
        
        elif (self.firstVal == other and self.secondVal == 0):
            return True
        #checks if one of the objects is initialized using another 
        
        return False
        #otherwise the objects aren't equal
    
    def __str__(object):
        message = str(object.firstVal) + "+" + str(object.secondVal) + \
                  "i"
        #message to be returned
        
        if (type(object.firstVal) == ComplexNumber):
            real = str(object.firstVal.firstVal)
            imaginary = str(object.firstVal.secondVal)
            return real + "+" + imaginary + "i"
                  
        return message
        #for the case of Complex Numbers initialized using other objects


    def realPart(self):
        if (type(self.firstVal) == int):
            return self.firstVal 
        #if the object was initialized using ints
        
        return self.firstVal.firstVal
        #if the object was initialized using other objects
        
    def imaginaryPart(self):
        if (type(self.firstVal) != int):
            return self.firstVal.secondVal 
        #if the object was initialized using other objects

        return self.secondVal
        #if the object was initialized using ints

    def getZero():
        if (ComplexNumber.zero == None):
            ComplexNumber.zero = ComplexNumber()
            #ensures that only one instance of zero is returned
        return ComplexNumber.zero
        





###############
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
    # you can do this:  type(obj).__n__
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

#################
def testComplexNumberClass():
    print("Testing ComplexNumber class... ", end="")
    # Do not use the builtin complex numbers in Python!
    # Only use integers!

    c1 = ComplexNumber(1, 2)
    assert(str(c1) == "1+2i")
    assert(c1.realPart() == 1)
    assert(c1.imaginaryPart() == 2)

    c2 = ComplexNumber(3)
    assert(str(c2) == "3+0i") # default imaginary part is 0
    assert(c2.realPart() == 3)
    assert(c2.imaginaryPart() == 0)

    c3 = ComplexNumber()
    assert(str(c3) == "0+0i") # default real part is also 0
    assert(c3.realPart() == 0)
    assert(c3.imaginaryPart() == 0)

    # Here we see that the constructor for a ComplexNumber
    # can take another ComplexNumber, which it duplicates
    c4 = ComplexNumber(c1)
    assert(str(c4) == "1+2i")
    assert(c4.realPart() == 1)
    assert(c4.imaginaryPart() == 2)

    assert((c1 == c4) == True)
    assert((c1 == c2) == False)
    assert((c1 == "Yikes!") == False) # don't crash here
    assert((c2 == 3) == True)

    s = set()
    assert(c1 not in s)
    s.add(c1)
    assert(c1 in s)
    assert(c4 in s)
    assert(c2 not in s)

    assert(ComplexNumber.getZero() == 0)
    assert(isinstance(ComplexNumber.getZero(), ComplexNumber))
    assert(ComplexNumber.getZero() == ComplexNumber())
    # This next one is the tricky part -- there should be one and
    # only one instance of ComplexNumber that is ever returned
    # every time you call ComplexNumber.getZero():
    assert(ComplexNumber.getZero() is ComplexNumber.getZero())
    # Hint: you might want to store the singleton instance
    # of the zero in a class attribute (which you should
    # initialize to None in the class definition, and then
    # update the first time you call getZero()).

    print("Passed!")

def testAll():
    testGateClasses()
    testComplexNumberClass()
    
def main():
    cs112_f17_week11_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()  

