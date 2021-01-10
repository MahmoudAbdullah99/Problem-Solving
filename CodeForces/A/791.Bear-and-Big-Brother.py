def years(lim_w, bob_w):
    years_needed = 0
    while True:
        lim_w *= 3
        bob_w *= 2
        years_needed += 1
        if lim_w > bob_w:
            return years_needed

if __name__ == "__main__":
    lim, bob = map(int, input().split())
    print(years(lim, bob))