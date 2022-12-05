# my email: labibkamal20@gmail.com

import random
from tempfile import tempdir

class poker:
    orderedCards = []
    nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suits = ['D', 'C', 'S', 'H']
    for i in suits:
            for j in nums:
                orderedCards.append(i+j)
    def __init__(self, players = 2):
        self.players = players
        self.decks = []
        for i in range(0, self.players):
            self.decks.append([])
        self.table = []
        #shuffle
        self.shuffledCards = []
        self.tempCards = poker.orderedCards.copy()
        for i in range(0, len(self.tempCards)):
            self.shuffledCards.append(self.tempCards.pop(random.randint(0, len(self.tempCards)-1)))
    def add_card(self, n):
        if n >= self.players:
           print('Player index out of range stoopid.')
           return
        self.decks[n].append(self.shuffledCards.pop(0))
    def add_to_table(self):
        self.table.append(self.shuffledCards.pop(0))
    def IsStraightFlush(self, lst):
        # returns True is all 5 cards in the list are of the same rank and of same order
        return 
    def IsFourofaKind(self, lst):
        # returns true of 4 of 5 cards of the list are of the same rank
        return
    def IsFullHouse(self, lst):
        # returns true of 3 cards are of same rank and 2 cards are of same rank
        return
    def IsFlush(self, lst):
        # returns true if all 5 cards have the same suit
        return
    def IsStraight(self, lst):
        # returns true if all 5 cards are in order
        return
    def IsThreeofaKind(self, lst):
        # returns true is 3 cards have the same rank
        return
    def IsTwoPairs(self, lst):
        # returns true if there are 2 pairs of cards of the same rank
        temp = lst.copy()
        pairs = 0
        for i in temp:
            for j in i[0]:
                for k in temp:
                    if j == k[0]:
                       pairs += 1
                       temp.pop(temp.index(i))
        if pairs >= 2:
            return True
        else:
            return False               
    
    def IsOnePair(self, lst): #Doesn't work cause its iterating over the the iteration twice.
        # returns true if there are 2 cards of the same rank
        for i in lst:
            for j in i[0]:
                for k in lst:
                    if j == k[0]:
                        return True
        return False
        
    
        
test = poker(5)
print(test.shuffledCards)
print(len(test.shuffledCards))
test.add_card(4)
print(test.decks)
test.add_to_table()
print(test.table)

                
        
        
        



        
        
        