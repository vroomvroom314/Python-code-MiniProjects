import copy
import cs112_f17_week7_linter

#By Shivum Agarwal
#Section G
#Collab with Andrew Ye and Ashwath Vijaykumar

"""Slow1 
1. This function creates a copy of a list and pops elements of it and returns 
   the length of the list itself
2. O(n)  
3. def fast1(a):
    c = len(a) 
    return c
4. Worst case, the time is O(1) because the len function is O(1) and 
that's the only function used so O(1) is the big-o runtime
"""

"""Slow2
1. This function returns duplicate of val within a list is equal to len(list)
2. O(n**2)  
3. def fast2(a):
    b = set(a) 
    return b = a 
4. Worst case, the time is O(n) because the only operation is the creation 
of the set which only adds each element of the list O(1) into
a set and the duplicates aren't included so this yield O(n)

"""

"""Slow3
1. This function returns the number of unique values in b compared to a
2. O(n**2)  
3. def fast3(a,b):
    set1 = set(a)
    set2 = set(b)
    return len(set2-set1)
4. Worst case, the time is O(n) because each set creation creates 
a new set of n elements so the p

"""

"""Slow4 
1. This function returns the biggest difference between an element of a and b
2. O(n**2)  
3. def fast4(a,b):
    a = a.sort() 
    b = b.sort() #sorts both lists
    changeA = abs(a[len(a)-1]-b[0]) #gets diff of biggest a and smallest b
    changeB = abs(b[len(b)-1]-a[0]) #gets diff of biggest a and smallest a
    
    if (changeA > changeB):
        return changeA
    return changeB
    #returns the bigger difference
    
4. Worst case, the time is O(nlogn) because the sorting function 
is O(nlogn) and all other functions are constant 
(getting index, finding difference)
"""

"""Slow5
1. This function returns the smallest difference between an element of a and b 
2. O(n**2)  
3. def fast5(a,b):
    a = a.sort()
    delta = fast4(a,b) #sets the initial difference to biggest between lists
    for c in b:
        Lowdelta = delta 
        Highdelta = delta
        d = bisect.bisect (a,c)
        a.insert(d,c) #inserts each c from b into a in ordered fashion
        if (c > a[0]):
            Lowdelta = a[d]-a[d-1] #sets Lowdelta to be compared to Highdelta
        if (c<a[len(a)-1]):
            Highdelta = a[d+1]-a[d] #sets Highdelta to be compared to Lowdelta
        if (Lowdelta > Highdelta):
            temp = Highdelta 
        else:
            temp = Lowdelta
        # sets the current smallest difference
        
        if (temp < delta):
            delta = temp
    return delta
    #returns the smallest overall delta between the lists
        
        
4. Worst case, the time is O(nlogn) because the sorting function 
is O(nlogn) and all other functions except Bisect 
are constant (getting index, finding difference) 
Bisect is O(logn).
"""

def largestSumOfPairs(a):
    #returns largest sum of pairs
    a1 = max(a)
    a.remove(a1)
    a2 = max(a)
    a.remove(a2)
    return (a1+a2)
    #removes the two largest elements of the list and returns their sum 
    #Take O(n) time because the functions max and remove are O(n)

def containsPythagoreanTriple(a):
    squareds = []
    for i in range (len(a)):
        squareds.append(a[i]**2)
    squareds.sort()
    #adds the squares of all the values within list a and sorts them
    #the appending takes O(n) and the sorting takes O(nlogn)

    for i in range (len(squareds)):
        j = 0 
        k = i
        #iterators that will go simulataneously through squareds list
        while (j <= i and k >= 0):
            if (squareds[j] + squareds[k] == squareds[i]):
                return True
                #finds a pythagorean triple and returns true
            elif (squareds[j] + squareds[k] > squareds[i]):
                k-=1
            #decrements k each time the sum of squares of j and k is too big
            elif (squareds[j] + squareds[k] < squareds[i]):
                j +=1
            #increments k each time the sum of squares of j and k is too small

    return False
    
def main():
    cs112_f17_week7_linter.lint() # check style rules


if __name__ == '__main__':
    main()
