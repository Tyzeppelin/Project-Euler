


def tailFacto(n, r):
    if n == 0:
        return r
    else :
        return tailFacto(n-1, r*n)


def factorial (n):
    return tailFacto(n, 1)



if __name__ == "__main__":

    print factorial(500)
