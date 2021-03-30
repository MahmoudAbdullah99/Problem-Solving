import itertools as it

n = int(input())
ls = input().split()
k = int(input())
c = 0
c1 = 0
for p in it.combinations(ls, k):
    c1 += 1
    if 'a' in p:
        c += 1

print("%.4f" %(c / c1))
