
import time

# It was solve in C .... Don't want to translate.
# Well... One liner.

if __name__ == "__main__":

    t1 = time.clock()

    print(max(filter(lambda x: str(x) == str(x)[::-1], [e*f for e in range(1000) for f in range(1000)])))

    print(time.clock() - t1, 'seconds')
