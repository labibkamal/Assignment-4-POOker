# my email: labibkamal20@gmail.com

import random

class poker:
    orderedCards = []
    nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suits = ['D', 'C', 'S', 'H']
    for i in nums:
            for j in suits:
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
        straight = poker.IsStraight(lst)
        flush = poker.IsFlush(lst)
        if straight and flush:
            return True
        else:
            return False
    def IsFourofaKind(self, lst):
        # returns true of 4 of 5 cards of the list are of the same rank
        lst_joined = ' '.join(lst)
        for i in lst:
            if lst_joined.count(i[0]) >= 4:
                return True 
        return False
    def IsFullHouse(self, lst):
        # returns true of 3 cards are of same rank and 2 cards are of same rank
        temp = lst.copy()
        lst_joined = ' '.join(lst)
        pair = 0
        trip = 0
        trip_rank = 0
        for i in temp:
            if lst_joined.count(i[0]) >= 3:
                trip = True
                trip_rank = i[0]
        for i in temp:
            if i != trip_rank and lst_joined.count(i[0]) >= 2:
                pair = True
        if trip and pair:
            return True
        else:
            return False
        
    def IsFlush(self, lst):
        # returns true if all 5 cards have the same suit
        lst_joined = ' '.join(lst)
        for i in lst:
            if lst_joined.count(i[1]) >= 5:
                return True 
        return False
    def IsStraight(self, lst):
        # returns true if all 5 cards are in order
        rank_only = []
        for i in lst:
            rank_only.append(i[0])
        temp = -1
        for i in poker.nums: 
            if i in rank_only: 
                temp = rank_only.index(i)
                break
        #print(temp)
        count = 1
        for i in range(temp, len(poker.nums)):
            if i < (len(poker.nums) - 1):
                if (poker.nums[i+1] in rank_only):
                    count += 1
                    continue
        print(count)
        if count >= 5:
            return True
        else: 
            return False
        
    def IsThreeofaKind(self, lst):
        # returns true is 3 cards have the same rank
        lst_joined = ' '.join(lst)
        for i in lst:
            if lst_joined.count(i[0]) >= 3:
                return True
        return False

    def IsTwoPairs(self, lst):
        # returns true if there are 2 pairs of cards of the same rank
        temp = lst.copy()
        temp_joined = ' '.join(temp)
        pairs = 0
        for i in temp:
            if temp_joined.count(i[0]) >= 2:
                pairs += 1
                temp.pop(temp.index(i))
        if pairs >= 2:
            return True
        else:
            return False               
    
    def IsOnePair(self, lst): 
        # returns true if there are 2 cards of the same rank
        lst_joined = ' '.join(lst)
        for i in lst:
            if lst_joined.count(i[0]) >= 2:
                return True
        return False


class TexasHoldem(poker):
    def __init__(self, players):
        super().__init__(players)
        
    def deal(self):
        for i in range(2):
            for i in range(self.players):
                super().add_card(i)
        for i in range(5):
            super().add_to_table()
        
    def check_hand(self, lst):
        if poker.IsStraightFlush(lst):
            return 'Straight Flush'
        elif poker.IsFourofaKind(lst):
            return 'Four of a Kind'
        elif poker.IsFullHouse(lst):
            return 'Full House'
        elif poker.IsFlush(lst):
            return 'Flush'
        elif poker.IsStraight(lst):
            return 'Straight'
        elif poker.IsThreeofaKind(lst):
            return 'Three of a Kind'
        elif poker.IsTwoPairs(lst):
            return 'Two Pairs'
        elif poker.IsOnePair(lst):
            return 'One Pair'
        else:
            return 'High Card'

    def hands(self):
        self.final_decks = []
        for i in poker.decks:
            self.final_decks.append(i + TexasHoldem.table)
        self.final_hands= []  
        for i in self.final_decks:
            self.final_hands.append(TexasHoldem.check_hand(i))
        print(self.final_hands)

    #def besthand(self):
        
    
test = poker(5)
#print(test.shuffledCards)
#print(len(test.shuffledCards))
test.add_card(4)
#print(test.decks)
test.add_to_table()
#print(test.table)        
final_test = TexasHoldem(5)
final_test.deal()
print(final_test.decks)
print(final_test.table)
final_test.hands()



                
        
        
        



        
        
        