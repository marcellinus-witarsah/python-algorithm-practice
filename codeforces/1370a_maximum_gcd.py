# find the maximum GCD
# greedy algorithm
def gcd_loop(a, b):
    lower = b if a >= b else a
    gcd = 0
    for d in range(1, lower + 1):
        if a % d == 0 and b % d == 0:
            gcd = d
    return gcd


# recursive way
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    cases = int(input())
    for c in range(cases):
        num = int(input())
        print(num//2)
    # naive solution (too slow)
    # for i in range(cases):
    #     max_gcd = 0
    #     num = int(input())
    #     for c1 in range(1, num + 1):
    #         for c2 in range(c1, num + 1):
    #             if c1 != c2:
    #                 max_gcd = max(max_gcd, gcd_loop(c1, c2))
    #     print(max_gcd)
    # recursive way
    # for i in range(cases):
    #     max_gcd = 0
    #     num = int(input())
    #     for c1 in range(1, num + 1):
    #         for c2 in range(c1, num + 1):
    #             if c1 != c2:
    #                 max_gcd = max(max_gcd, gcd_recursive(c2, c1))
    #     print(max_gcd)
    # eucledian way
    # for i in range(cases):
    #     max_gcd = 0
    #     num = int(input())
    #     for c1 in range(1, num + 1):
    #         for c2 in range(c1, num + 1):
    #             if c1 != c2:
    #                 max_gcd = max(max_gcd, gcd_euclidean(c2, c1))
    #     print(max_gcd)
