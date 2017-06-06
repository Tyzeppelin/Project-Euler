
import collections
import itertools
import operator
import time

from operator import itemgetter


value = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}


# We define a value function for each poker hand
# I could have chosen a denser code, but this one was drafted on a corner of paper
# and it 'works' so ...
# 
# Highest card      -> card value
# Pair              -> 14**1 * pair value
# Two pairs         -> 14**2 * 14*highest pair + second pair
# Three of a kind   -> 14**3 * value
# Straight          -> 14**4 * highest straight card
# Flush             -> 14**5 * highest flush card
# Full House        -> 14**6 + brelan value + pair value
# Four of a kind    -> 14**7 * value
# Straight Flush    -> 14**8 * highest card value
# Royal Flush       -> 14**9  

class Hand:


    def __init__(self, hand):
        
        #print(hand)
        self._hand = sorted([(value[a[0]], a[1]) for a in hand], key=itemgetter(0))
        self._is_flush = len(set([c[1] for c in self._hand])) == 1
        self._heights = [a[0] for a in self._hand]
        self._nb_pairs, self._pairs = self._has_pairs()
        self._is_straight = reduce(lambda it,x:it and x, [a+1 == b for (a,b) in zip(self._heights[:4], self._heights[1:])])
        #print(type(self._pairs))

    def _has_pairs(self):
        c = 0
        pairs = []
        for i in range(0,4):
            if self._heights[i] == self._heights[i+1]:
                c+=1
                pairs.append(self._heights[i])
        return c, sorted(pairs)

    def get_value(self):
        # royal flush
        if self._is_flush and sum(self._heights) == 55:
            self.value = 14**9
        # straight flush
        elif self._is_flush and self._is_straight:
            self.value = 14**8 * self._heights[-1]
        # four of a kind
        elif len(set(self._heights[:4])) == 1 or \
                len(set(self._heights[1:])) == 1:
            self.value = 14**7 * self._heights[2]
        # full house
        elif (len(set(self._heights[:3])) == 1 and len(set(self._heights[3:])) == 1) or \
                (len(set(self._heights[:2])) == 1 and len(set(self._heights[2:])) == 1):
            self.value = 14 ** 6 \
                        + 14**3 * self._heights[2] \
                        + 14**2 * self._heights[0 if self._heights[0] != self._heights[2] else 4]
        #flush
        elif self._is_flush:
            self.value = 14**5 * self._heights[4]
        # straight
        elif self._is_straight:
            self.value = 14**4 * self._heights[4]
        # three of a kind
        elif len(set(self._heights[2:])) == 1 or \
                len(set(self._heights[:3])) == 1 or \
                len(set(self._heights[1:4])) == 1:
            self.value = 14**3 * self._heights[2]
        # two pairs
        elif self._nb_pairs == 2:
            self.value = 14**2 + 14 * max(self._pairs) + min(self._pairs)
        # pair
        elif self._nb_pairs == 1:
            self.value = 14 * self._pairs[0]
        # highest value
        else:
            self.value = self._heights[4]
        return self.value

 
if __name__ == "__main__":

    t1 = time.clock()

    with open("poker.txt", 'r') as f:
        games = [s.rstrip().split(' ') for s in f.readlines()]
   
    #p1 = Hand(['5C','3C','2S','AS','4C'])
    #print(p1.get_value())

    c = 0
    for g in games:
        p1 = Hand(g[:5])
        p2 = Hand(g[5:])

        if p1.get_value() > p2.get_value():
            #print('p1 victory ->', p1.get_value(), p1._hand, p2.get_value(), p2._hand)
            c += 1
        elif p1.get_value() == p2.get_value():
            #print('tie', p1._hand, p2._hand)
            for (c1, c2) in reversed(zip(p1._heights, p2._heights)):
                if c1 > c2:
                    #print('p1 victory ->', c1,c2,p1.get_value(), p1._heights, p2.get_value(), p2._heights)
                    c += 1
                    break
                elif c2 > c1:
                    break
        #else:
            #print('p2 victory', p1.get_value(), p1._hand, p2.get_value(), p2._hand)
    print(c)
    print(time.clock() - t1, "seconds")
