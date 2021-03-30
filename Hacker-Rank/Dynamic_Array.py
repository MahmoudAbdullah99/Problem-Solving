def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    n_arr = []

    for i in range(len(queries)):
        if queries[i][0] == 1:
            seqList[(queries[i][1]^lastAnswer)%n].append(queries[i][2])
        
        elif queries[i][0] == 2:
            seq = seqList[(queries[i][1]^lastAnswer)%n]
            lastAnswer = seq[queries[i][2] % len(seq)]
            n_arr.append(lastAnswer)

    return n_arr


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    for i in range(len(result)):
        print(result[i])
