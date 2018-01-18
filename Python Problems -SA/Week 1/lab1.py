#################################################
# Lab1
#################################################

import cs112_f17_linter
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

#################################################
# Lab1 problems
#################################################

def nearestOdd(n):
    x = n%2
    if (x==1):
        return n
    elif (x==0):
        return n-1
    else:
        if (x>0.5):
            a = math.ceil(n)
            return a-1
        else:
            a = roundHalfUp(n)
            return a+1
            
            
    return x

def rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    
    if ((x1+w1<x2) or (x2+w2<x1) or y1+h1<y2 or y2+h2<y1):
        return False
    else: 
        return True
       
    
    
        

    return 42


def isPerfectSquare(n):
    
    if not isinstance(n,int):
        return False
    elif n%1 != 0 :
        return False
    elif n<0:
        return False
    else:
        root = n**0.5
        if (root % 1) ==0:
            return True
        else :
            return False
    
def getKthDigit(n, k):    
    if (n<0):
        y = abs(n)
        x = (y//(10**k))%10
        return x
    else:
        x = (n//(10**k))%10
        return x
    
    
def setKthDigit(n, k, d):
    if (n<0):
        num = abs(n)
        x = getKthDigit(num,k)
        y = num-(10**k*x)
        final = y + (d*(10**k))
        return final*-1
    
    else:
        x = getKthDigit(n,k)
        y = n-(10**k*x)
        final = y + (d*(10**k))
        return final

def colorBlender(rgb1,rgb2,midpoints,n):
    red1 = rgb1//10**6
    green1 = ((rgb1 - red1*10**6)//10**3)
    blue1 = rgb1 - (red1*10**6)-(green1*10**3)
    
   

    red2 = rgb2//10**6
    green2 = ((rgb2 - red2*10**6)//10**3)
    blue2 = rgb2 - (red2*10**6)-(green2*10**3)
 
   
    if (n<0 or n > midpoints + 1):
        return None
    
    else:
        redDiff = (red2 * n + red1 * (midpoints - n +1))/(midpoints+1)
        if (redDiff%1!=0 and redDiff>0.5):
            redDiff = roundHalfUp(redDiff)
        else:
            redDiff = int(redDiff)
        greenDiff = (green2 * n + green1 * (midpoints - n +1))/(midpoints+1)
        if (greenDiff%1!=0 and greenDiff>0.5):
            greenDiff = roundHalfUp(greenDiff)
        else:
            greenDiff = int(greenDiff)
        blueDiff = (blue2 * n + blue1 * (midpoints - n +1))/(midpoints+1)
        if (blueDiff%1!=0 and blueDiff>0.5):
            blueDiff = roundHalfUp(blueDiff)
        else:
            blueDiff = int(blueDiff)
    return redDiff * 10**6 + greenDiff * 10**3 + blueDiff
                
                
                
        
        

#################################################
# Lab1 Test Functions
################################################

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    print('Passed.')

def testRectanglesOverlap():
    print('Testing rectanglesOverlap()...', end='')
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3,4,5,6) == False)
    print('Passed.')

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(1234**2) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(17) == False)
    assert(isPerfectSquare(-16) == False)
    assert(isPerfectSquare(1234**2+1) == False)
    assert(isPerfectSquare(1234**2-1) == False)
    assert(isPerfectSquare(4.0000001) == False)
    assert(isPerfectSquare('Do not crash here!') == False)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed.')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed.')

#################################################
# Lab1 Main
################################################

def testAll():
    testNearestOdd()
    testRectanglesOverlap()
    testIsPerfectSquare()
    testGetKthDigit()
    testSetKthDigit()
    testColorBlender()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        'as,break,class,continue,del,except,finally,for,' +
        'global,in,is,lambda,nonlocal,pass,raise,repr,' +
        'try,while,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,range,repr,reversed,set,' +
        'setattr,slice,sorted,staticmethod,str,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_f17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
