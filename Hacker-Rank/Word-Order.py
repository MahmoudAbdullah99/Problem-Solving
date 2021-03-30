if __name__ == "__main__":
    n = int(input())
    arr = []
    dict = {}
    for i in range(n):
        key = input()
        if key not in dict:
            dict[key] = 1
        else:
            dict[key] += 1
    print(len(dict))
    print(" ".join([str(i) for i in dict.values()]))