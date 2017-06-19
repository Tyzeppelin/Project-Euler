
import collections
import time

from collections import defaultdict

if __name__ == "__main__":

    t1 = time.clock()

    prev = defaultdict(set)
    key = ''

    with open('keylog.txt', 'r') as f:
        triplet = set([l.rstrip() for l in f.readlines()])
    
    chars = set([v for t in triplet for v in t])
    for a,b,c in triplet:
        prev[b].add(a)
        prev[c].add(b)
   
    len_key = len(prev) + 1

    while len(key) < len_key:
        f = filter(lambda x: len(prev[x]) == 0 and x not in key, chars)[0]
        del prev[f]
        chars.remove(f)
        prev = {k:[w for w in v if w != f] for k,v in prev.iteritems()}
        key += f
 
    print(key)
    print(time.clock() - t1, "seconds")
