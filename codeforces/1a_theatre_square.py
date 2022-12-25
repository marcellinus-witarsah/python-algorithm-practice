import math

if __name__ == "__main__":
    m, n, a = list(map(int, str(input()).split()))
    print(math.ceil(m / a) * math.ceil(n / a))
