from datetime import datetime

# Complete the time_delta function below.
def time_delta(time1, time2):
    frmt = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(time1,frmt)
    t2 = datetime.strptime(time2,frmt)
    return int(abs((t1-t2).total_seconds()))
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)