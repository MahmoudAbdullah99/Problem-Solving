from itertools import groupby
print(*[(len(list(p[1])), int(p[0])) for p in groupby(input())])