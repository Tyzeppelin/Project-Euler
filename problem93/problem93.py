
import collections
import functools
import itertools
import operator
import time

# not working
# I have written / solved this a long time ago
# and I don't have the patience of goign though this again

def longest_continuous_subsequence(arr, numbers):
    sorted_arr = sorted(arr)
    if sorted_arr[0] != 1:
        return 0
    prev = 0
    seq = 0
    # add max_seq when else and return max(max_seq, seq)
    for x in sorted_arr:
        if x == prev + 1:
            seq += 1
        else:
            break
        prev = x
    return seq


if __name__ == "__main__":

    t1 = time.time()

    operators = [ operator.add, operator.sub, operator.mul, operator.truediv ]

    seqs = collections.defaultdict(lambda: set())
    res = {}
    ints = 0
    for numbers in itertools.combinations(range(1, 10), 4):
        for nums in itertools.permutations(numbers, 4):
            for ops in itertools.product(operators, repeat=3):
                for order in itertools.permutations((1, 2, 3), 3):
                    val = functools.reduce(lambda b, z: z[0](b, z[1]), zip(ops, nums[1:]), nums[0])
                    if val > 0 and val % 1 == 0.0:
                        seqs[numbers].add(val)
                        ints += 1
        res[numbers] = longest_continuous_subsequence(seqs[numbers], numbers)

    print(res)
    max_id = max(res, key=res.get)
    print(ints, max_id, res[max_id])

    print("done under", time.time() - t1, "seconds.")
