def main():
    n = int(input())

    st = input().strip()

    counter = 0
    for i in range(n-1):
        if st[i] == st[i+1]:
            counter+=1

    print(counter)

if __name__ == "__main__":
    main()