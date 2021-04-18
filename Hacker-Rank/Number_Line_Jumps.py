def main():
    x1, v1, x2, v2 = get_input()
    print(calculate(x1, v1, x2, v2))


def get_input():
    x1, v1, x2, v2 = map(int, input().split())
    return x1, v1, x2, v2


def calculate(x1, v1, x2, v2):
    if x1 == x2 and v1 == v2:
        return 'YES'
    elif (x1 == x2 and v1 != v2) or (x1 != x2 and v1 == v2):
        return 'NO'
    if (x1-x2) / (v1-v2) >= 0:
        return 'NO'
    if abs(x1-x2) % abs(v2-v1) == 0:
        return 'YES'
    return 'NO'


if __name__ == "__main__":
    main()
    # print(5 % 0)