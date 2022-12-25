if __name__ == "__main__":
    k, n = list(map(int, str(input()).split()))
    arr = list(map(int, str(input()).split()))
    count = 0
    thresh = arr[n - 1]
    for element in arr:
        if element >= thresh and element > 0:
            count += 1
    print(count)
