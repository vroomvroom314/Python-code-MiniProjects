#################################################
# Lab3
#################################################

import cs112_f17_week3_linter
import math
import sys

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

def getTotalandCount(namegrade,total,count):
    grade = int(namegrade)
    total+=grade 
    count+=1
    
    return total,count

    

#################################################
#By Shivum Agarwal
#shivuma

def longestCommonSubstring(s1, s2):
    start = 0
    currentend = 1
    currentrun = ""
    longestcommon = ""
    currentcommon = ""
    bestcommonlen = 0
    currentlen = 0
    #sets range and variables for nested for loop
    for i in range (len(s1)):
        for j in range (start + 1, len(s1)):
            currentsubstring = s1[i:j+1]
    #nested loop goes through s1 and takes a substring 
            if (currentsubstring in s2):
                currentcommon = currentsubstring
                currentlen = len(currentcommon)
                #checks if substring is in s2 and sets new var for it
                if (currentlen > bestcommonlen):
                    bestcommonlen = currentlen
                    longestcommon = currentcommon
                #checks and updates the longest string length into vars above
                elif (len(currentsubstring) ==  bestcommonlen and
                 currentsubstring < longestcommon):
                     longestcommon = currentsubstring
                #sets the longest common string after other if statements
    return longestcommon



def bestStudentAndAvg(gradebook):
    beststudent = ""
    bestaverage = -sys.maxsize-1
    name = ""
    #sets variables for the best student and average that is to be returned
    #sets variable "name" for student's name
    for line in gradebook.splitlines():
    #loops through each specific line of gradebook to access name and grades
        total = 0
        count = 0
        #variables used for calculating average grade
        if((line.startswith("#") or line == "")):  
                continue
        #ensures that no errors occur due to empty space or hashtags
        for namegrade in line.split(","):
            #splits names and grades in gradebook
            if (namegrade.isdigit()):
                total,count = getTotalandCount(namegrade,total,count)
                #returns the total and count of the scores of a single student
            elif (namegrade.isalpha()):
                name = namegrade
                #sets the name of student in the specific line
            elif ("-" in namegrade):
                total,count = getTotalandCount(namegrade,total,count)
                #takes into account the "-" and gets total and count 
        average = total/count
        #calculates the average score of a specific student
        if (average >= bestaverage):
            beststudent = name
            bestaverage = average
        #sets the name of the student of student with highest score
    return (beststudent+":"+str(int(bestaverage)))
    #returns the name of best student and returns a string instance of score

def encodeColumnShuffleCipher(message, key):
    remainder = len(message)%len(key)
    newMessage = ""
    finalMessage = ""
    #sets variables to be used for finding final message given the key
    if (remainder != 0):
        message = message + ("-"*(len(key)-remainder))
        #fills up the rest of message with "-" 
    for i in range(len(key)): 
        for c in message[i:len(message):len(key)]:
            newMessage += c
            #adds character for every keyth index
    for c in key:
        c = int(c)
        increment = int(len(message)/len(key))
        #sets the step for final change in message
        finalMessage += newMessage[c*increment:c*increment+increment]
        #sets final message 
    return key+finalMessage    
    
    

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    assert(longestCommonSubstring("fgheduhAHSN", "fghAHSN") == "hAHSN")
    print("Passed!")

def testBestStudentAndAvg():
    print("Testing bestStudentAndAvg()...", end="")
    gradebook = """
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:92")
    gradebook   =   """
#   ignore  blank   lines   and lines   starting    with    #'s
wilma,93,95

fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:94")
    gradebook = "fred,0"
    assert(bestStudentAndAvg(gradebook) ==  "fred:0")
    gradebook = "fred,-1\nwilma,-2"
    assert(bestStudentAndAvg(gradebook) ==  "fred:-1")
    gradebook = "fred,100"
    assert(bestStudentAndAvg(gradebook) ==  "fred:100")
    gradebook = "fred,100,110"
    assert(bestStudentAndAvg(gradebook) ==  "fred:105")
    gradebook = "fred,49\nwilma" + ",50"*50
    assert(bestStudentAndAvg(gradebook) ==  "wilma:50")
    print("Passed!")
    
def testEncodeColumnShuffleCipher():
    print("Testing encodeColumnShuffleCipher()...", end="")
    
    msg = "WEATTACKATDAWN"
    result = "0213WTAWACD-EATNTKA-"
    assert(encodeColumnShuffleCipher(msg, "0213") == result)
    
    msg = "SUDDENLYAWHITERABBITWITHPINKEYESRANCLOSEBYHER"
    result = "210DNAIRBWHNYRCSYRUEYHEBTTIESNOBESDLWTAIIPKEALEH"
    assert(encodeColumnShuffleCipher(msg,"210") == result)

    print("Passed!")
    

#################################################
# testAll and main
#################################################

def testAll():
    testLongestCommonSubstring()
    testBestStudentAndAvg()
    testEncodeColumnShuffleCipher()

def main():
    cs112_f17_week3_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
