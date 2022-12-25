if __name__ == "__main__":
    user_in = int(input())

    for i in range(1, user_in+1):
        a = user_in - i
        if a % 2 == 0 and i % 2 == 0 and a != 0:
            print("YES")
            quit()
    print("NO")

