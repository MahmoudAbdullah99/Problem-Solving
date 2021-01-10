def needed_money(k, n, w):
    needed = (int)(k*w*(w+1)/2) - n
    return needed if needed >= 0 else 0

if __name__ == "__main__":
    k, n, w = map(int, input().split())
    print(needed_money(k, n, w))