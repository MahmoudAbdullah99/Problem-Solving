def main():
    user_na = input().strip()
    print_reply(is_odd(distinct(user_na)))

def distinct(user_name):
    return set(user_name)

def is_odd(dist_chs):
    return len(dist_chs) % 2 != 0

def print_reply(bool):
    print('IGNORE HIM!') if bool else print("CHAT WITH HER!")

if __name__ == "__main__":
    main()


# you can write a two line code for this but the readability will be low
# user_name = user_na = input().strip()
# print('IGNORE HIM!') if len(set(user_name)) % 2 != 0 else print("CHAT WITH HER!")