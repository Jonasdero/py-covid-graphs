import datetime


def getDate(usString):
    return datetime.datetime.strptime(usString, "%m/%d/%y").date()


def addDays(date, amount):
    return date + datetime.timedelta(days=amount)


def addOneDay(date):
    return addDays(date, 1)


def daterange(startDate, endDate):
    for n in range(int((endDate - startDate).days)+1):
        yield startDate + datetime.timedelta(n)
