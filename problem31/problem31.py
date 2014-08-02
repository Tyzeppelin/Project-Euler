import time

# TODO : Regarder la fin du tp6 d'ocaml. Il y a un algo de partition


def nextCurrency(c):
#   print l, c
    curr_ptr = currency.index(c)
    if curr_ptr == 0 :
        return 0
    else :
        return currency[curr_ptr-1]


# A modifier pour prendre en compte les valeurs de `currency`
def part(n, k):
    if n == 0 and k == 0:
        #print "P(",n,",",k,")"
        return 1
    elif k == 0:
        #print "P(",n ,",",k,")"
        return 0
    elif k > n:
        #print "P(",n ,",",k,")", "P(",n ,",",n,")"
        return part(n, n)
    else:
        #print "P(",n ,",",k,")","&&","P(", n-k, ",", k, ") &&", "P(", n, ",",nextCurrency(k),")"
        return part(n-k, k) + part(n, nextCurrency(k))

if __name__ == "__main__":
    t1 = time.clock()

    currency = [1, 2, 5, 10, 20, 50, 100, 200]
    #currency = [1,2,3,4,5,6]

#    a = [[], [1], [2,3,4]]
#    print insert(a, 4)

    #print part(6, currency[-1])
    a = part(200, currency[-1])
    print a
    print "Completed in", time.clock()-t1, "seconds"
