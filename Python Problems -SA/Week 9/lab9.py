#################################################
# Lab9
#
# No iteration! no 'for' or 'while'.  Also, no 'zip' or 'join'.
# You may add optional parameters
# You may use wrapper functions
#
#################################################

import cs112_f17_week9_linter
import math

def almostEqual(x, y, epsilon = 10**-8):
    return abs(x-y) < epsilon

##############################################
# Recursive questions
##############################################
#By Shivum Agarwal
#Section G
#Collab with Andrew Ye and Ashwath Vijaykumar


def alternatingSum(L):
    if (L == []):
        return 0
    #base case ensuring that the summation breaks
    else:
        return L.pop(0) - alternatingSum(L)
    #pops first element of list and recursively adds or subtracts next sum

def powersOf3ToN(n, k =1):
    if (n < 1):
        return None
    #gets rid negatives
    elif (k > n): 
        return []
    #base case to ensure that no more powers of three exist
   
    else: 
        if (k <= n):
            return [k] + powersOf3ToN(n, k*3)
            #recursively adds next power three until it reaches close to val n
    


def binarySearchValues(L, v, low = 0, high = None):
    if (high == None):
        high = len(L)-1
    #sets the highest index for binary search, None is a placeholder
    
    mid = (low+high)//2
    #gets the middle value
    
    if low > high:
        return []
    #prevents crashing if low > high, bad error
    
    if (L[mid] == v):
        return [(mid,L[mid])]
    #base case, finds the correct letter and its index that is to be returned
    
    elif (L[mid] > v):
        return [(mid,L[mid])]+ binarySearchValues(L, v, low, mid-1)
    #narrows the list to be looped through if mid value is higher than v
    
    elif (L[mid] < v):
        return  [(mid,L[mid])]+ binarySearchValues(L, v, mid+1, high)
    #narrows the list to be looped through if mid value is lower than v



##############################################
# OOP questions
##############################################

class Book(object):
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author 
        self.pages = pages
        self.currentPage = 1
        self.markedPage = None
    #initializes all necessary variables to be used in the class
    
    def __eq__(self, other):
        if isinstance(other, Book):
           if (self.title == other.title and self.author == other.author 
               and self.pages == other.pages and self.currentPage == 
               other.currentPage and self.markedPage == other.markedPage):
                   return True
        #checks if all initialized variables in init for two books match
        else:
            return False
        #if any variable in init is different, the books are not the same
            
            
    def __repr__(self):
        if (self.pages == 1 and self.markedPage == None):
            return "Book<%s" % self.title + " by %s" % self.author + \
                ": %d" % self.pages + " page, currently on page " + \
                "%d" % self.currentPage + ">"
        #book contains 1 page only
        
        elif (self.markedPage == None): 
            return "Book<%s" % self.title + " by %s" % self.author + \
                ": %d" % self.pages + " pages, currently on page " + \
                "%d" % self.currentPage + ">"
        #book contains multiple pages but has no bookmark

        else:
            return "Book<%s" % self.title + " by %s" % self.author + \
                ": %d" % self.pages + " pages, currently on page " + \
                "%d" % self.currentPage + ", page " + \
                "%d" % self.markedPage + " bookmarked" ">"
        #for every other type of book

    def turnPage(self,pageturn):       
        self.pageturn = pageturn
        self.currentPage += self.pageturn
        #turns the page for whatever input is given
        
        if (self.currentPage > self.pages):
            self.currentPage = self.pages
        #prevents turning to page outside of book length
            
        if (self.currentPage < 1):
            self.currentPage = 1
        #prevents turning to page outside of book length

        
        
    def placeBookmark(self):
        self.markedPage = self.currentPage
        #sets a bookmark on given page
    
    def getBookmarkedPage(self):
        if (self.markedPage == None):
            return None
        #no bookmark location is returned if no bookmark is placed
        else: 
            return self.markedPage
        #locations of bookmark is returned
    
    def turnToBookmark(self):
        if (self.markedPage != None):
            self.currentPage = self.markedPage  
        #goes to the page where bookmark exists
    
    def removeBookmark(self):
        if (self.markedPage != None):
            self.markedPage = None
        #gets rid of book mark if it exists
        
    def getCurrentPage(self):
        return self.currentPage
        #gets the current page that the user is on
        
        
        
    pass

#################################################
# Test Functions
#################################################

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    print('Done!')

def testPowersOf3ToN():
    print('Testing powersOf3ToN()...', end='')
    assert(powersOf3ToN(-42) == None)
    assert(powersOf3ToN(0.99) == None)
    assert(powersOf3ToN(1) == [1])
    assert(powersOf3ToN(3) == [1, 3])
    assert(powersOf3ToN(8.9999) == [1, 3])
    assert(powersOf3ToN(9) == [1, 3, 9])
    assert(powersOf3ToN(9.1111) == [1, 3, 9])
    assert(powersOf3ToN(100) == [1, 3, 9, 27, 81])
    print('Done!')


def testBinarySearchValues():
    print('Testing binarySearchValues()...', end='')
    L = ['a', 'c', 'f', 'g', 'm', 'q']
    assert(binarySearchValues(L, 'a') == [(2,'f'), (0,'a')])
    assert(binarySearchValues(L, 'c') == [(2,'f'), (0,'a'), (1,'c')])
    assert(binarySearchValues(L, 'f') == [(2,'f')])
    assert(binarySearchValues(L, 'g') == [(2,'f'), (4, 'm'), (3, 'g')])
    assert(binarySearchValues(L, 'm') == [(2,'f'), (4, 'm')])
    assert(binarySearchValues(L, 'q') == [(2,'f'), (4, 'm'), (5, 'q')])
    assert(binarySearchValues(L, 'z') == [(2,'f'), (4, 'm'), (5, 'q')])
    assert(binarySearchValues(L, 'b') == [(2,'f'), (0,'a'), (1,'c')])
    print('Done!')

def testBookClass():
    print("Testing Book class...", end="")
    # A Book has a title, and author, and a number of pages.
    # It also has a current page, which always starts at 1. There is no page 0!
    book1 = Book("Harry Potter and the Sorcerer's Stone", 
                 "J. K. Rowling", 309)
    assert(str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " + 
                         "J. K. Rowling: 309 pages, currently on page 1>")
    book2 = Book("Carnegie Mellon Motto", "Andrew Carnegie", 1)
    assert(str(book2) == "Book<Carnegie Mellon Motto by Andrew Carnegie: " +
                         "1 page, currently on page 1>")
                         
    # You can turn pages in a book. Turning a positive number of pages moves
    # forward; turning a negative number moves backwards. You can't move past
    # the first page going backwards or the last page going forwards
    book1.turnPage(4) # turning pages does not return
    assert(book1.getCurrentPage() == 5)
    book1.turnPage(-1)
    assert(book1.getCurrentPage() == 4)
    book1.turnPage(400)
    assert(book1.getCurrentPage() == 309)
    assert(str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " + 
                         "J. K. Rowling: 309 pages, currently on page 309>")
    book2.turnPage(-1)
    assert(book2.getCurrentPage() == 1)
    book2.turnPage(1)
    assert(book2.getCurrentPage() == 1)
    
    # You can also put a bookmark on the current page. This lets you turn
    # back to it easily. The book starts out without a bookmark.
    book3 = Book("The Name of the Wind", "Patrick Rothfuss", 662)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 1>")
    assert(book3.getBookmarkedPage() == None)
    book3.turnPage(9)
    book3.placeBookmark() # does not return
    assert(book3.getBookmarkedPage() == 10)
    book3.turnPage(7)
    assert(book3.getBookmarkedPage() == 10)
    assert(book3.getCurrentPage() == 17)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 17, page 10 bookmarked>")
    book3.turnToBookmark()
    assert(book3.getCurrentPage() == 10)
    book3.removeBookmark()
    assert(book3.getBookmarkedPage() == None)
    book3.turnPage(25)
    assert(book3.getCurrentPage() == 35)
    book3.turnToBookmark() # if there's no bookmark, don't turn to a page
    assert(book3.getCurrentPage() == 35)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 35>")
    
    # Finally, you should be able to compare two books directly
    book5 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book6 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book7 = Book("A Natural History of Dragons", "Marie Brennan", 334)
    book8 = Book("A Game of Spoofs", "George R.R. Martin", 807)
    assert(book5 == book6)
    assert(book5 != book7)
    assert(book5 != book8)
    book5.turnPage(1)
    assert(book5 != book6)
    book5.turnPage(-1)
    assert(book5 == book6)
    book6.placeBookmark()
    assert(book5 != book6)
    print("Done!")

##############################################
# testAll and main
##############################################

def testAll():
    testAlternatingSum()
    testPowersOf3ToN()
    testBinarySearchValues()
    testBookClass()

def main():
    cs112_f17_week9_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
