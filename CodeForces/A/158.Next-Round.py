def next_round(n, km, numbers):
    res = 0
    for number in numbers:
        if number >= numbers[k - 1] and number !=0: res +=1
    return res
 
if __name__ == "__main__":
    n, k = list(map(int, input().split(' ')))
    ls = list(map(int, input().split(' ')))
    print(next_round(n, k, ls))