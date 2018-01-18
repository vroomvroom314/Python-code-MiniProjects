import copy
import cs112_f17_week7_linter
import time


#By Shivum Agarwal
#shivuma
#Section G


def invertDictionary(d):
    reverseDict = {}
    #creates dictionary to contain reverse
    for key, val in d.items():
        reverseDict.setdefault(val, set()).add(key)
        #puts the val in set in the pos of key and adds the original key for val
    return reverseDict
    
def friendsOfFriends(d):
    finaldict = {}
    keys = []
    for key,val in d.items():
        keys.append(key)
    #adds key elements to list
    
    for i in range (len(keys)):
        tempSet1 = d[keys[i]]
        #gets the values of each key in the list
        Valset = set()
        #used to contain all friends of friends per key
        for j in range (len(keys)):
            if (keys[j] in tempSet1):
                tempSet2 = d[keys[j]]
                #gets the values of each value in the original key
                for k in range (len(keys)):
                    if (keys[k] in tempSet2 and keys[k] not in tempSet1 and
                        keys[k] != keys[i]):
                        Valset.add(keys[k])
                        #adds new element if it's not the same as the orig key 
                        #new element must also not be original vals of key 
                        #new element must be vaue of original key's value
                    finaldict[keys[i]] = Valset
        if d[keys[i]] == set():
            finaldict[keys[i]] = set()
            #adds all keys that have empty sets or "no friends" to finaldict 

    return finaldict
    
 
    
def instrumentedSelectionSort(a):
    start_time = time.time()
    #sets the start time of program
    n = len(a)
    compCount = 0
    swapCount = 0
    #creates variables to be returned
    for startIndex in range(n):
        minIndex = startIndex
        count = 0
        #init conditions of sort
        for i in range(startIndex+1, n):
            if (a[i] < a[minIndex]):
                minIndex = i
                #gets index with lowest value
            count+=1
            #increments count of comparison per iteration
        compCount += count
        #adds up each count for a final big comparison count
        swap(a, startIndex, minIndex)
        #swaps the actual elements
        swapCount += 1
        #swapCount increases for each swap that occurs

    
    return compCount,swapCount, ("--- %s seconds ---" % (time.time()
                                - start_time))
    #returns the number of comparisons, swaps, and program time

def instrumentedBubbleSort(a):
    start_time = time.time()
    #sets the start time of program
    n = len(a)
    end = n
    swapped = True
    #vars used for the while loop below
    compCount = 0
    swapCount = 0
    #creates variables to be returned
    while (swapped):
    #while loop used for going through swap conditions
        count = 0
        swapped = False
        #sets init conditions 
        for i in range(1, end):
            if (a[i-1] > a[i]):
                swap(a, i-1, i)
                #swaps the actual elements
                swapCount +=1
                swapped = True
            #increments swap count for each swap and sets the condition to true
            count+=1
            #increments count of comparison per iteration

        compCount += count
        #adds up each count for a final big comparison count
        end -= 1
        #lowers the ending point to get closer to final sort
    
    return compCount, swapCount, ("--- %s seconds ---" % (time.time()
                                - start_time))
    #returns the number of comparisons, swaps, and program time


def selectionSortvsBubbleSort():
    a = [3,4,2,1]
    print("BubbleSort: ", instrumentedBubbleSort(a))
    #prints the properties of BubbleSort given the list a
   
    a = [3,4,2,1]
    print("SelectionSort: ", instrumentedSelectionSort(a))
    #prints the properties of SelectionSort given the list a

    
    
def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])
    #swaps two values given the list and its indexes

def testInstrumentedSelectionSort():
    print("Testing instrumentedSelectionSort...")
    comparisons, swaps, time = instrumentedSelectionSort([3,7,4,0])
    assert(comparisons == 6)
    assert(swaps == 4)
    comparisons, swaps, time = instrumentedSelectionSort([3, 2])
    assert(comparisons == 1)
    assert(swaps == 2)
    print("You did it!")


def main():
    cs112_f17_week7_linter.lint() # check style rules
    testInstrumentedSelectionSort()

if __name__ == '__main__':
    main()
