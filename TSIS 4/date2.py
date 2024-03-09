import datetime

def ytt():
    today = datetime.datetime.now()
    yesterday = datetime.datetime(today.year, today.month, today.day - 1)
    tomorrow = datetime.datetime(today.year, today.month, today.day + 1)



    print("Yesterday is ", yesterday)
    print("Today is ", today)
    print("Tomorrow is ", tomorrow)


ytt()
