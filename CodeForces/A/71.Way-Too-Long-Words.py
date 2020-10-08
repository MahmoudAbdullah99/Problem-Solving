if __name__ == "__main__":
    n = int(input())
    ls = []

    for i in range(n):
        ls.append(input())

    for i in range(n):
        ln = len(ls[i])
        if ln > 10:
            print(ls[i][0] + str(ln - 2) + ls[i][ln - 1])
        else:
            print(ls[i])