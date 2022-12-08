lst = ['2H', '6D', '5D', '8C', '8S']
nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

def IsFullHouse(lst):
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

print(IsFullHouse(lst))
        
    



   