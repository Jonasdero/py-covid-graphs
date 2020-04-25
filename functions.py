import requests
import csv
from date import getDate, addOneDay


def getCSV(csvURL):
    with requests.Session() as s:
        download = s.get(csvURL)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        return my_list


def transformCountries(csvList):
    countries = {}

    defRow = csvList[0]

    lowestRowIndex = 4
    highestRowIndex = len(defRow)-1

    startDate = getDate(defRow[lowestRowIndex])
    endDate = getDate(defRow[highestRowIndex])

    for index in range(1, len(csvList)-1):
        row = csvList[index]
        country = row[1]
        countryData = {}
        if countries.get(country) is None:
            countryData['startDate'] = startDate
            countryData['endDate'] = endDate
            countryData['lat'] = row[2]
            countryData['long'] = row[3]
            countryData['timeSeries'] = parseTimeSeries(row)
            countries[country] = countryData
        else:
            mergeTimeSeries(countries[country].get(
                'timeSeries'), parseTimeSeries(row))
    return countries


def parseTimeSeries(row):
    timeSeries = []

    for index in range(4, len(row)):
        timeSeries.append(int(row[index]))

    return timeSeries


def mergeTimeSeries(timeSeries1, timeSeries2):
    for i in range(0, len(timeSeries1)):
        timeSeries1[i] += timeSeries2[i]
    return timeSeries1
