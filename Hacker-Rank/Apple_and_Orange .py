def main():
    s, t, a, b, apples_dist, oranges_dist = get_input()
    count_and_print(s, t, a, b, apples_dist, oranges_dist)


def count_and_print(s, t, a, b, apples_dist, oranges_dist):
    count_apples, count_oranges = 0, 0
    for i in apples_dist:
        if i + a in range(s, t + 1):
            count_apples += 1

    for i in oranges_dist:
        if i + b in range(s, t + 1):
            count_oranges += 1

    print(count_apples, count_oranges, sep='\n')


def get_input():
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())
    apples_dist = list(map(int, input().split()))
    oranges_dist = list(map(int, input().split()))
    return s, t, a, b, apples_dist, oranges_dist


if __name__ == "__main__":
    main()
