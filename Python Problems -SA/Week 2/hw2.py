#################################################
# Hw2
#################################################

import cs112_f17_week2_linter
import math

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

# Put your solution to getKthDigit here!
def getKthDigit(n, k):    
    if (n<0):
        y = abs(n)
        x = (y//(10**k))%10
        return x
    else:
        x = (n//(10**k))%10
        return x

# Put your solution to numberLength here!
def numberLength(x):
    y = abs(x) 
    #Accounts for negative numbers
    digits = 0
    #Counter for total digits  
    while (y>0):
        y //= 10
        digits += 1
    #keeps dividing number until 0 and digits increments as well
    return digits

# Put your solution to isPrime here!
def isPrime(n):
    if (n < 2):
        return False
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True



#################################################

def containsOddDigits(x):
    while (x>0):
    #loops through number 
        digit = x%10
        #takes onesdigit
        if (digit % 2 !=0 and digit != 0) :
            return True
        #checks for odds digit 
        x //=10
        #divides to find next digit
    return False

def countMultiplesOfSeven(x, y):
    sevencount = 0
    #sets count for sevens
    if (y>x):
        for i in range (x,y+1):
            if (i % 7 == 0 and i!=0):
                sevencount +=1
            #checks if divisible by seven
        return sevencount
    return sevencount
    

def printNumberTriangle(n):
    for i in range (n):
        #rows for triangle
        for j in range (i+1):
            print (i+1-j,end = "")
            #prints the actual vals for the triangle
        print("")
        #used for creating new line
    
            
    
def sumOfSquaresOfDigits(x):
    sum = 0
    #sets sum
    while (x>0):
        digit = x%10
        #gets digit
        squared = digit**2
        #squares digit
        sum += squared
        #adds squared to sum
        x //=10
        #divides to find next digit
    return sum
        
def isHappyNumber(x):
    if (x<1):
        return False
    #Immediately gets rid of negatives
    if (x == 1):
        return True
    #1 is happy so true is automatically returned
    while (x!=1):
        x = sumOfSquaresOfDigits(x)
        #gets sum of squares
        if (x == 1):
            return True
        #returns True for happy numbers
        if (x==4):
            return False
        #ensures that nonHappy numbers are returned as false
        
    return False

def nthHappyPrime(n):
    guess = 0
    #used for actual value of HappyPrime
    found = -1
    #used for the counter of HappyPrime
    i = 0
    #Iterator for while loop
    if (n<0):
        return None
    #gets rid of negative numbers
    while (found < n):
        if (isPrime(i) and isHappyNumber(i)): 
        #checks if i is prime and if is a happy number
            guess = i
            #guess becomes i
            found += 1
            #found increments
        i+=1    
        #i continues to increment
    return guess
    
    

##### Bonus #####

def play112(game):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testContainsOddDigits():
    print('Testing containsOddDigits()... ', end='')
    assert(containsOddDigits(1246) == True)
    assert(containsOddDigits(8663) == True)
    assert(containsOddDigits(224) == False)
    assert(containsOddDigits(115) == True)
    assert(containsOddDigits(8) == False)
    assert(containsOddDigits(9) == True)
    print('Passed!')

def testCountMultiplesOfSeven():
    print('Testing countMultiplesOfSeven()... ', end='')
    assert(countMultiplesOfSeven(3, 16) == 2)
    assert(countMultiplesOfSeven(13, 15) == 1)
    assert(countMultiplesOfSeven(7, 22) == 3)
    assert(countMultiplesOfSeven(8, 28) == 3)
    assert(countMultiplesOfSeven(15, 18) == 0)
    assert(countMultiplesOfSeven(15, 6) == 0)
    print('Passed!')

def testPrintNumberTriangle():
    import sys, io
    print('Testing printNumberTriangle()... ', end='')
    tmpOut = sys.stdout

    oneOutput = io.StringIO()
    sys.stdout = oneOutput
    printNumberTriangle(1)
    oneCheck = oneOutput.getvalue()

    fourOutput = io.StringIO()
    sys.stdout = fourOutput
    printNumberTriangle(4)
    fourCheck = fourOutput.getvalue()

    sevenOutput = io.StringIO()
    sys.stdout = sevenOutput
    printNumberTriangle(7)
    sevenCheck = sevenOutput.getvalue()

    sys.stdout = tmpOut

    assert(oneCheck == "1\n")
    assert(fourCheck == "1\n21\n321\n4321\n")
    assert(sevenCheck == "1\n21\n321\n4321\n54321\n654321\n7654321\n")
    print('Passed!')

def testSumOfSquaresOfDigits():
    print('Testing sumOfSquaresOfDigits()... ', end='')
    assert(sumOfSquaresOfDigits(5) == 25)
    assert(sumOfSquaresOfDigits(12) == 5)
    assert(sumOfSquaresOfDigits(234) == 29)
    print('Passed!')

def testIsHappyNumber():
    print('Testing isHappyNumber()... ', end='')
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print('Passed!')

def testNthHappyPrime():
    print('Testing nthHappyPrime()... ', end='')
    assert(nthHappyPrime(0) == 7)
    assert(nthHappyPrime(1) == 13)
    assert(nthHappyPrime(2) == 19)
    assert(nthHappyPrime(3) == 23)
    assert(nthHappyPrime(4) == 31)
    assert(nthHappyPrime(5) == 79)
    assert(nthHappyPrime(6) == 97)
    print('Passed!')

def testBonusPlay112():
    print("Testing play112()... ", end="")
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testContainsOddDigits()
    testCountMultiplesOfSeven()
    testPrintNumberTriangle()
    testSumOfSquaresOfDigits()
    testIsHappyNumber()
    testNthHappyPrime()
    testBonusPlay112()

def main():
    cs112_f17_week2_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
