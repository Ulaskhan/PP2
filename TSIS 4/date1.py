import datetime

def minus5days():
    date = datetime.datetime.now()
    b = datetime.datetime(date.year, date.month, date.day - 5)
    print("5 days ago ", b)
minus5days()
