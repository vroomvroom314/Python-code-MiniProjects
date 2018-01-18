#################################################
# Hw9
#
# No iteration! no 'for' or 'while'.  Also, no 'zip' or 'join'.
# You may add optional parameters
# You may use wrapper functions
#
#################################################

import cs112_f17_week9_linter
import string

def almostEqual(x, y, epsilon = 10**-8):
    return abs(x-y) < epsilon

##############################################
# Recursive questions
##############################################
#By Shivum Agarwal
#Section G
#shivuma


def powerSum(n, k):
    if (n == 1):
        return 1**k
    #base case, the powersum is multiplied by this final value
    if (n<0):
        return 0
    #deals with negative numbers 
    if (k<0):
        return 0
    #ensures a positive exponent 
    else:
        return n**k + powerSum(n-1,k)
    #recursively adds the sum for each n**k until n decreases to 1.
    

def isHappyNumber(n):
    if (n<1):
        return False
    #a number cant be happy if less than 1 so it's automatically false
    if (n == 1):
        return True
    #base case for happy numbers, the sum = 1 so initial num is happy
    if (n == 4):
        return False
    #base case for non-happy numbers, sum will never reach 1 so unhappy number
            
    else:
        x = sumOfSquaresOfDigits(n)
        #gets the sum of the squares of digits of the num given in this case
        return isHappyNumber(x)
        #recursive function that's looped to get if num happy
    
def sumOfSquaresOfDigits(x):
    if (x == 0):
        return 0
    #base case when x is integer divided all the way to 0
    else:
        return (x%10)**2 + sumOfSquaresOfDigits(x//10)
        #gets the digit squared and recursively continues for each digit 


def evalPrefixNotation(L, nums = []):
    if (L == []):
        return nums.pop()
    #base case that returns the final value of the equation 
    else:
        x = L.pop()
        #gets the last element of the prefix expression
        if (x == "*" or x == "+" or x == "-"):
            operand1 = nums.pop()
            operand2 = nums.pop()
            #gets the first two operands if x is an operation
            if (x == "*"):
                result = operand1*operand2
                nums.append(result)
                #multiplies operands and puts that value back in nums
                return evalPrefixNotation(L)
                #updates list of nums in equation to be evaluated again
            elif (x == "+"):
                result = operand1+operand2
                nums.append(result)
                #adds operands and puts that value back in nums
                return evalPrefixNotation(L)
                #updates list of nums in equation to be evaluated again
            elif (x == "-"):
                result = operand1-operand2
                nums.append(result)
                #subtracts operands and puts that value back in nums
                return evalPrefixNotation(L)
                #updates list of nums in equation to be evaluated again
        else: 
            nums.append(x)
            #updates the list of nums with new number at end of list
            return evalPrefixNotation(L)
            #updates list of nums in equation to be evaluated again


    

##############################################
# OOP questions
##############################################

class VendingMachine(object):
    
    def __init__(self, bottles, price):
        self.bottles = bottles
        self.initPrice = price
        self.price = price 
        self.excessMoney = 0
    #initializes a Vending Machine object
       
    def __repr__(self):
        
        if (self.bottles == 1):
            if (self.initPrice % 100 ==0):
                return "Vending Machine:<%d" % self.bottles + " bottle; $" + \
                "%d" % (self.initPrice/100)  + " each; $0 paid>"
            else:    
                return "Vending Machine:<%d" % self.bottles + " bottle; $" + \
                "%0.2f" % (self.initPrice/100) + " each; $0 paid>"
            
        else:
            if (self.initPrice-self.price == 0):
                Ins = "%0.0f" % (self.initPrice/100-self.price/100) + " paid>"
                return "Vending Machine:<%d" % self.bottles + " bottles; $" + \
                    "%0.2f" % (self.initPrice/100) + " each; $" + Ins
            else:
                Ins = "%0.2f" % (self.initPrice/100-self.price/100) + " paid>"
                return "Vending Machine:<%d" % self.bottles + " bottles; $" + \
                    "%0.2f" % (self.initPrice/100) + " each; $" + Ins
                    
        #returns a statement about the given object 
                    
    def __eq__(self, other):
        if isinstance(other, VendingMachine):
            if (self.bottles == other.bottles and self.price ==
                other.price):
                return True
            #checks if the # of bottles and price of bottle is equal
            else:
                return False
            #returns false if otherwise
    
    def __hash__(self):
        return hash(self.price)
        #gets the hash value depending on the price
    
    def isEmpty(self):
        if (self.bottles == 0):
            return True
        return False
        #returns whether or not there are bottles in the vending machine

    
    def getBottleCount(self):
        return self.bottles
        #returns the number of bottles left in vending machine object
    
    def insertMoney(self, money):
        self.moneyInserted = money        
        if (self.moneyInserted > self.price):
            self.excessMoney += self.moneyInserted-self.price
            self.price = 0
            #checks if user inputs more money than needed to buy drink
        else:
            self.price = self.price - self.moneyInserted
            #updates the amount of money needed to buy a drink

        if (self.price == 0):
            if (self.bottles > 0):
                self.bottles -= 1
                self.price = self.initPrice
                return (("Got a bottle!", self.excessMoney))
                #if a drink is bought, the num of bottles is updated 
                #price is re-initialized
                
        if (self.bottles == 0):
            self.price = self.initPrice
            return (("Machine is empty", money))
            #returns that the machine is empty if no bottles are left
            
        elif (self.price % 100 == 0 and self.price > 0 and self. bottles > 0):
            return (("Still owe $" + str(self.price//100), self.excessMoney))
       
        elif (self.price % 100 != 0 and self.price > 0 and self. bottles > 0):
            return (("Still owe $" + "%0.2f" % (self.price/100), 
                    self.excessMoney))
        #returns the amount of money that is still owed 

        
    def stockMachine(self, moreBottles):
        self.bottles += moreBottles
        #adds bottles to vending machine
        
    def stillOwe(self):
        return self.price 
        #returns the amount that is needed to be deposited 
    
    pass

#################################################
# Test Functions
#################################################

def testPowerSum():
    print('Testing powerSum()...', end='')
    assert(powerSum(4, 6) == 1**6 + 2**6 + 3**6 + 4**6)
    assert(powerSum(0, 6) == 0)
    assert(powerSum(4, 0) == 1**0 + 2**0 + 3**0 + 4**0)
    assert(powerSum(4, -1) == 0)
    print('Done!')

def testIsHappyNumber():
    print('Testing isHappyNumber()...', end='')
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print('Done!')

def testEvalPrefixNotation():
    print('Testing evalPrefixNotation()...', end='')
    assert(evalPrefixNotation([42]) == 42)
    assert(evalPrefixNotation(['+', 3, 4]) == 7)
    assert(evalPrefixNotation(['-', 3, 4]) == -1)
    assert(evalPrefixNotation(['-', 4, 3]) == 1)
    assert(evalPrefixNotation(['+', 3, '*', 4, 5]) == 23)
    assert(evalPrefixNotation(['+', '*', 2, 3, '*', 4, 5]) == 26)
    assert(evalPrefixNotation(['*', '+', 2, 3, '+', 4, 5]) == 45)
    assert(evalPrefixNotation(['*', '+', 2, '*', 3, '-', 8, 7,
                               '+', '*', 2, 2, 5]) == 45)
    print('Done!')

def testVendingMachineClass():
    print("Testing Vending Machine class...", end="")
    # Vending machines have three main properties: 
    # how many bottles they contain, the price of a bottle, and
    # how much money has been paid. A new vending machine starts with no
    # money paid.
    vm1 = VendingMachine(100, 125)
    assert(str(vm1) == "Vending Machine:<100 bottles; $1.25 each; $0 paid>")
    assert(vm1.isEmpty() == False)
    assert(vm1.getBottleCount() == 100)
    assert(vm1.stillOwe() == 125)
    
    # When the user inserts money, the machine returns a message about their
    # status and any change they need as a tuple.
    assert(vm1.insertMoney(20) == ("Still owe $1.05", 0))
    assert(vm1.stillOwe() == 105)
    assert(vm1.getBottleCount() == 100)
    assert(vm1.insertMoney(5) == ("Still owe $1", 0))
    
    # When the user has paid enough money, they get a bottle and 
    # the money owed resets.
    assert(vm1.insertMoney(100) == ("Got a bottle!", 0))
    assert(vm1.getBottleCount() == 99)
    assert(vm1.stillOwe() == 125)
    assert(str(vm1) == "Vending Machine:<99 bottles; $1.25 each; $0 paid>")
    
    # If the user pays too much money, they get their change back with the
    # bottle.
    assert(vm1.insertMoney(500) == ("Got a bottle!", 375))
    assert(vm1.getBottleCount() == 98)
    assert(vm1.stillOwe() == 125)
    
    # Machines can become empty
    vm2 = VendingMachine(1, 120)
    assert(str(vm2) == "Vending Machine:<1 bottle; $1.20 each; $0 paid>")
    assert(vm2.isEmpty() == False)
    assert(vm2.insertMoney(120) == ("Got a bottle!", 0))
    assert(vm2.getBottleCount() == 0)
    assert(vm2.isEmpty() == True)
    
    # Once a machine is empty, it should not accept money until it is restocked.
    assert(str(vm2) == "Vending Machine:<0 bottles; $1.20 each; $0 paid>")
    assert(vm2.insertMoney(25) == ("Machine is empty", 25))
    assert(vm2.insertMoney(120) == ("Machine is empty", 120))
    assert(vm2.stillOwe() == 120)
    vm2.stockMachine(20) # Does not return anything
    assert(vm2.getBottleCount() == 20)
    assert(vm2.isEmpty() == False)
    assert(str(vm2) == "Vending Machine:<20 bottles; $1.20 each; $0 paid>")
    assert(vm2.insertMoney(25) == ("Still owe $0.95", 0))
    assert(vm2.stillOwe() == 95)
    vm2.stockMachine(20)
    assert(vm2.getBottleCount() == 40)
    
    # We should be able to test machines for basic functionality
    vm3 = VendingMachine(50, 100)
    vm4 = VendingMachine(50, 100)
    vm5 = VendingMachine(20, 100)
    vm6 = VendingMachine(50, 200)
    vm7 = "Vending Machine"
    assert(vm3 == vm4)
    assert(vm3 != vm5)
    assert(vm3 != vm6)
    assert(vm3 != vm7) # should not crash!
    s = set()
    assert(vm3 not in s)
    s.add(vm4)
    assert(vm3 in s)
    s.remove(vm4)
    assert(vm3 not in s)
    assert(vm4.insertMoney(50) == ("Still owe $0.50", 0))
    assert(vm3 != vm4)
    print("Done!")

##############################################
# testAll and main
##############################################

def testAll():
    testPowerSum()
    testIsHappyNumber()
    testEvalPrefixNotation()
    testVendingMachineClass()

def main():
    cs112_f17_week9_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()  