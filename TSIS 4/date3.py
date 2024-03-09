import datetime


def dropm():
    x = datetime.datetime.now()
    x1 = x.replace(microsecond=0)
    print(x1)
dropm()