if __name__ == "__main__":
    n_probs = int(input())
    count = 0
    for i in range(n_probs):
        user_in = list(map(int, str(input()).split()))
        if sum(user_in) >= 2:
            count += 1
    print(count)

