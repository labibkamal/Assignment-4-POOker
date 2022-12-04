import random

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
        self.decks[n].append(self.shuffledCards.pop(0))
    def add_to_table(self):
        self.table.append(self.shuffledCards.pop(0))
        
test = poker()
print(test.shuffledCards)
print(len(test.shuffledCards))
test.add_card(1)
print(test.decks)
test.add_to_table()
print(test.table)

                
        
        
        



        
        
        