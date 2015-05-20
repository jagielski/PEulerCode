from itertools import groupby

class Card:
    def __init__(self, str):
        self.val = str[0]
        self.suit = str[1]
    
    def value(self):
        if self.val == 'T':
            return 10
        if self.val == 'J':
            return 11
        if self.val == 'Q':
            return 12
        if self.val == 'K':
            return 13
        if self.val == 'A':
            return 0
        else:
            return int(self.val)

pokerfile = open("p054_poker.txt")
pokerhands = []
for line in pokerfile:
    pokerhands.append([[Card(card) for card in line.split()[:5]],[Card(card) for card in line.split()[5:]]])
def score(hand):
    if isflush(hand):
        if isstraight(hand) == 2:
            return (10,'')
        if isstraight(hand) == 1:
            return (9,max([c.value() for c in hand]))
        return (6,max([c.value() for c in hand]))
    if isstraight(hand):
        return (5,max([c.value() for c in hand]))
    if maxgroup(hand)[0] != []:
        if len(maxgroup(hand)[0]) == 1:
            if maxgroup(hand)[0][0][1] == 3:
                return (4,maxgroup(hand)[1])
            elif maxgroup(hand)[0][0][1] == 4:
                return (8, maxgroup(hand)[1])
            else:
                return (2, maxgroup(hand)[1])
        else:
            if maxgroup(hand)[0][0][1] == 2 and maxgroup(hand)[0][1][1]==2:
                return (3, maxgroup(hand)[1])
            else:
                return (7, maxgroup(hand)[1])
    else:
        return (1,maxgroup(hand)[1])
            
    
def isflush(hand):  
    return hand[0].suit == hand[1].suit and hand[0].suit == hand[2].suit and hand[0].suit == hand[3].suit and hand[0].suit == hand[4].suit
    
def isstraight(hand):
    sortedhand = sorted(hand, key = lambda card: card.value())
    if sortedhand[0].value() == sortedhand[1].value()-1 and sortedhand[1].value() == sortedhand[2].value()-1 and sortedhand[2].value() == sortedhand[3].value()-1 and sortedhand[3].value() == sortedhand[4].value()-1:
        return 1
    elif sortedhand[0].value() == 0 and sortedhand[1].value() == 2 and sortedhand[2].value() == 3 and sortedhand[3].value() == 4 and sortedhand[4].value() ==5:
        return 1
    elif sortedhand[0].value() == 0 and sortedhand[1].value() == 10 and sortedhand[2].value() == 11 and sortedhand[3].value() == 12 and sortedhand[4].value() ==13:
        return 2
    return 0
    
def maxgroup(hand):
    sortedvals = sorted([c.value() for c in hand])
    groups = []
    prevval = sortedvals[0]
    count = 0
    for val in sortedvals:
        if prevval == val:
            count+=1
        else:
            if count>1:
                groups.append((prevval, count))
            prevval = val
            count = 1
    if count>1:
        groups.append((val, count))
    remlist = [x for x in sortedvals if not x in [el[0] for el in groups]]
    if len(remlist)>0:
        return groups, max(remlist)
    else:
        return groups, max([x[0] for x in groups])
            
count = 0
doublecount = 0
triplecount = 0
for handpair in pokerhands:
    score1 = score(handpair[0])
    score2 = score(handpair[1])
    if score1[0]>score2[0]:
        count+=1
    elif score1[0]== score2[0]:
        doublecount +=1
        if score1[1]>score2[1]:
            triplecount +=1
            count+=1
print(count,doublecount, triplecount)        