from collections import Counter


def happiness(arr, A, B):
    hpns = 0
    for i, c in Counter(arr).items():
        if i in A:
            hpns += c
        elif i in B:
            hpns -= c
    return hpns


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    print(happiness(arr, A, B))