lst = ['2H', '6S', '9H', '8C', 'QS']

lst_joined = ' '.join(lst)
print(lst_joined)
def IsTwoPairs(lst):
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

print(IsTwoPairs(lst))


'''def IsOnePair(lst):  ### Not working, check j and k values
        # returns true if there are 2 cards of the same rank
        for i in lst:
            for j in i[0]:
                for k in lst:
                    print(j)
                    print(k)
                    if j == k[0]:
                        return True
        return False

print(IsOnePair(lst))'''

'''
def IsTwoPairs(lst):
        # returns true if there are 2 pairs of cards of the same rank
        temp = lst.copy()
        #print(temp)
        pairs = 0
        for i in temp:
            for j in i[0]:
                for k in temp:
                    if j == k[0]:
                        pairs += 1
                        print(pairs)
                        temp.pop(temp.index(k))
                       
        if pairs >= 2:
            return True
        else:
            return False  
        
print(IsTwoPairs(lst)) '''     