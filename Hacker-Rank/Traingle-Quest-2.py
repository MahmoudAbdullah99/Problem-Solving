n = int(input())
for i in range(1, n+1):
    print(int((1+10**i*(-2+10**i)//81)))
