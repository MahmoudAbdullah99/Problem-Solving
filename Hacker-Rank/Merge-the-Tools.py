def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s = string[i : i+k]
        ss = ''
        for j in s:
            if j not in ss:
                ss += j
        print(ss)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)