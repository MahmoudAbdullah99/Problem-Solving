from calendar import weekday
if __name__ == "__main__":
    month, day, year = (map(int, input().split()))
    days = ['MONDAY', 'TUESDAY',  'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    print(days[weekday(year, month, day)])