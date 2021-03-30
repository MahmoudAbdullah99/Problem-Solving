def minion_game(s):
    ke, st = 0, 0
    vo = 'AEIOU'
    for i in range(len(s)):
        if s[i] in vo:
            ke += len(s) - i
        else:
            st += len(s) - i
    if ke > st:
        print("Kevin", ke)
    elif ke < st:
        print("Stuart", st)
    else:
            print("Draw")
            
if __name__ == '__main__':
    s = input()
    minion_game(s)