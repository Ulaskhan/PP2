import datetime

def difseconds(b):
    now = datetime.datetime.now()
    now_seconds = now.timestamp()
    b_seconds = b.timestamp()

    print(now_seconds - b_seconds, " seconds")
b = datetime.datetime(2005, 10, 17)
difseconds(b)
