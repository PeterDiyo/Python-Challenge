'''
PROBLEM: 
 Alice has some cards with numbers written on them. She arranges the cards in decreasing 
 order, and lays them out face down in a sequence on a table. She challenges Bob to pick 
 out the card containing a given number by turning over as few cards as possible. Write a 
 function to help Bob locate the card
'''
#Linear_search

def locate_card(cards, query):
    for position in range (0, len(cards)):
        if cards[position] == query:
            return position
    return -1    


#Example usage
cards = [13,10,9,6,4,2,1,0]
query = 4
result = locate_card(cards, query)
print(result)