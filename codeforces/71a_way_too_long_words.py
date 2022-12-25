if __name__ == "__main__":
    cases = int(input())
    for i in range(cases):
        usr_in = str(input())
        usr_in_len = len(usr_in)
        # if the len is below or equal to 0
        if usr_in_len <= 10:
            print(usr_in)
        else:
            # slice the word from index 1 to n-1
            t = usr_in[1:-1]
            print("{}{}{}".format(usr_in[0], len(t), usr_in[-1]))
