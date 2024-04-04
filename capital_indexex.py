'''
Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.
For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
'''

def capital_indexes (word):
    capital_indexes = []
    for i, char in enumerate(word):
        if char.isupper():
            capital_indexes.append(i)
    return capital_indexes 


#Example usage
word = "lEtERs"
result = capital_indexes (word)
print(result)

'''
Check out Leetcode, GforG
'''