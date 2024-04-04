'''
QUESTION 1.
PROBLEM: 
 Alice has some cards with numbers written on them. She arranges the cards in decreasing 
 order, and lays them out face down in a sequence on a table. She challenges Bob to pick 
 out the card containing a given number by turning over as few cards as possible. Write a 
 function to help Bob locate the card
'''

#Binary_search

def locate_card(cards, query):
    low = 0
    high = len(cards) - 1
    while low <= high:
        mid = (low + high) // 2
        position = cards[mid]
        if position == query:
            return mid
        elif position < query:
            high = mid - 1
        elif position > query:
            low = mid + 1
    return -1        


'''
QUESTION 2.
If the list has duplicates, especially if our query is more than one value;

E.g [8,8,6,6,6,6,6,6,3,2,2,2,0,0,0]

if Query = 6,
then Expected Out(first occurrence) = 2(index)
But, Binary Search Reyurns = 7(index) on first attempt

SOLUTION: When cards[mid] = query, chck whether it is the first occurrence of the query
in the list.
'''
#Solution: Define a helper_function called test_location, which take; cards, query and mid as arguments
def test_location (cards, query, mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return "left"
        else:
            return "found"
    elif cards[mid] < query:
        return "left"
    else:
        return "right"
        
#Update our program by calling the above function.
def locate_card(cards, query):
    low = 0
    high = len(cards) - 1
    while low <= high:
        mid = (low + high) // 2
        result = test_location(cards, query, mid) #function call
        if result == "found":
            return mid
        elif result == "left":
            high = mid - 1
        elif result == "right":
            low = mid + 1
    return -1         



'''
QUESTION 3.

Generic Algorithm for Binary search(binary_search function)
'''
def binary_search (low, high, condition):
    while low <= high:
        mid = (low + high) // 2
        result = condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            high = mid - 1
        else:
            low = mid + 1
    return -1            

'''
QUESTION: give an array of integer numbers in ascending order, find the starting and
ending position of a given number.
'''
#We are looking for both the the start index and the end index
'''
a. having already created our binary_search function;
1. write two functions, (i)first_position and (ii)last_position, 
2. return binary_search function in each one of them,
3. create another function called first_and_last_position and return both the first_position
   function and the last_position function in it.

Note: all the functions put together will still have a complexity of O(log N).
'''
def first_position (nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return "left"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(nums)-1, condition) #binary_search() call 

def last_position (nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return "right"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(nums)-1, condition) #binary_search() call


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target) #first_position() and #last_position() call


#check out Leetcode question, GeeksForGeeks.