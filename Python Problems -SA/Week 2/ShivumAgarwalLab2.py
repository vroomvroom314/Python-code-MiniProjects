#################################################
# Lab2
#################################################

import cs112_f17_week2_linter
import math

#################################################
# Helper functions
#################################################

#ShivumAgarwal

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

# See if you can rewrite isPrime from lecture here!
def isPrime(n):
    if (n < 2):
        return False
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True

#################################################

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


def countMatchingDigits(x, y):
    matchingDigits = 0
    #set counter for matching digits
    Xlength = numberLength(x)
    Ylength = numberLength(y)
    #get lengths for both x and y
    for i in range(Xlength):
        #loops through x
        Xdigit = getKthDigit(x,i)
        #gets digit for x
        for j in range(Ylength):
        #loops through y
            Ydigit = getKthDigit(y,j)
            #gets digit for y
            if (Xdigit == Ydigit):
                matchingDigits +=1
            #increments matchingdigits for each instance of match
            
    return matchingDigits        


def rotateNumber(x):
    xlength = numberLength(x)
    #set number of digits in x
    if (xlength == 1):
        return x
    #one digit numbers stay the same
    val = x%10
    #gets onesdigit
    y = x//10
    #integer divides original number by ten 
    newx = val*10**(xlength-1)+y
    #new number is the sum of val multiplied by 10 to a certain power plus y
    return newx

def isCircularPrime(x):
    count = 0
    #sets count
    xlength = numberLength(x)
    #sets length
    if (x == 0):
        return False
    #avoides the logic error of 0 being a prime
    if (not isPrime(x)):
        return False
    #prevents even numbers from being recognized as circular primes
    while (count < xlength):
        x = rotateNumber(x)
        if (not isPrime(x)):
            return False 
        count +=1
    return True
    #rotates numbers and checks if they're prime
    

def nthCircularPrime(n):
    found = 0
    guess = 0
    i = 0
    #sets variables for counter and the circular prime numbers/indexes
    while (found <= n):
        if (isCircularPrime(i)):
            guess = i
            found += 1
        i+=1
    #loops until found reaches n and guess is the actual nth circularprime
    return guess
            
def reverseNum(n):
    reverse = 0
    #establishes variable for reversed num
    while (n>0):
        onesdigit = n%10
        #gets onesdigit
        reverse = reverse*10+onesdigit
        #adds reverse to opposite of n
        n = n //10
        #int divide n to reach next digit
    return reverse
    
def nthEmirpsPrime(n):
    found = 0
    guess = 0
    i = 10
    #sets variables for counter and the circular prime numbers/indexes

    while (found <= n):        
        if (i == reverseNum(i)):
            i+=1
        #skips instances where reverse of n is the same as n
        if (isPrime(i) and isPrime(reverseNum(i))):                
            guess = i
            found += 1 
            #set guess to current value in loop and increments found
        i+=1
    return guess
            

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testNumberLength():
    print('Testing numberLength()... ', end='')
    assert(numberLength(12) == 2)
    assert(numberLength(3) == 1)
    assert(numberLength(89) == 2)
    assert(numberLength(12345) == 5)
    assert(numberLength(120021) == 6)
    assert(numberLength(5000) == 4)
    print('Passed!')

def testCountMatchingDigits():
    print('Testing countMatchingDigits()... ', end='')
    assert(countMatchingDigits(1234, 2071) == 2)
    assert(countMatchingDigits(2203, 1527) == 2)
    assert(countMatchingDigits(5, 1253) == 1)
    assert(countMatchingDigits(18737, 7) == 2)
    assert(countMatchingDigits(1220, 7322) == 4)
    assert(countMatchingDigits(1234, 5678) == 0)
    print('Passed!')

def testRotateNumber():
    print('Testing rotateNumber()... ', end='')
    assert(rotateNumber(1234) == 4123)
    assert(rotateNumber(4123) == 3412)
    assert(rotateNumber(3412) == 2341)
    assert(rotateNumber(2341) == 1234)
    assert(rotateNumber(5) == 5)
    assert(rotateNumber(111) == 111)
    print('Passed!')

def testIsCircularPrime():
    print('Testing isCircularPrime()... ', end='')
    assert(isCircularPrime(2) == True)
    assert(isCircularPrime(11) == True)
    assert(isCircularPrime(13) == True)
    assert(isCircularPrime(79) == True)
    assert(isCircularPrime(197) == True)
    assert(isCircularPrime(1193) == True)
    print('Passed!')

def testNthCircularPrime():
    print('Testing nthCircularPrime()... ', end='')
    assert(nthCircularPrime(0) == 2)
    assert(nthCircularPrime(4) == 11)
    assert(nthCircularPrime(5) == 13)
    assert(nthCircularPrime(11) == 79)
    assert(nthCircularPrime(15) == 197)
    assert(nthCircularPrime(25) == 1193)
    print('Passed!')

def testNthEmirpsPrime():
    print('Testing nthEmirpsPrime()... ', end='')
    assert(nthEmirpsPrime(0) == 13)
    assert(nthEmirpsPrime(5) == 73)
    assert(nthEmirpsPrime(10) == 149)
    assert(nthEmirpsPrime(20) == 701)
    assert(nthEmirpsPrime(30) == 941)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testNumberLength()
    testCountMatchingDigits()
    testRotateNumber()
    testIsCircularPrime()
    testNthCircularPrime()
    testNthEmirpsPrime()

def main():
    cs112_f17_week2_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
