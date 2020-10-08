if __name__ == "__main__":
    s = input().lower()
    ls1 =[]
    for i in s:
        if i not in 'aoyeui':
            ls1.append('.')
            ls1.append(i)
    st = ''.join(ls1)
    print(st)