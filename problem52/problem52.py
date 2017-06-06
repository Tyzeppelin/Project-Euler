
import time

def iterator():
    i = 1
    exp = 1
    exp6 = 10**exp/6
    while True:
        if i < exp6:
            yield i
            i += 1
        else:
            #print 'break -> ', i, exp6
            i = 10**exp
            exp += 1
            exp6 = 10**exp / 6
        
def to_str_sort(x):
    m = map(int, str(x))
    m.sort()
    return m

if __name__ == "__main__":

    t1 = time.clock()

    for e in iterator():
        m = to_str_sort(e)
        m2 = to_str_sort(e*2)
        m3 = to_str_sort(e*3)
        m4 = to_str_sort(e*4)
        m5 = to_str_sort(e*5)
        m6 = to_str_sort(e*6)
        if m == m2 == m3 == m4 == m5 == m6:
            print e
            break

    print time.clock() - t1, "seconds"
