
from functions.date import getDate, addOneDay
from constantData.keys import confirmedKey, deathsKey, endDateKey, latKey, lonKey, newConfirmedKey, newDeathsKey, newRecoveredKey, recoveredKey, startDateKey, percentageConfirmedKey, percentageDeathsKey, percentageRecoveredKey, activeKey, newActiveKey, percentageActiveKey, nameKey, latestActiveKey, latestDeathsKey, latestRecoveredKey


def parseData(confirmedList, deathList, recoveredList):
    countries = {}

    # Lists are nearly the same, therefore only the first list (confirmedList) is taken for indexing or dates
    defRow = confirmedList[0]

    lowestRowIndex = 4
    highestRowIndex = len(defRow)-1

    startDate = getDate(defRow[lowestRowIndex])
    endDate = getDate(defRow[highestRowIndex])

    for index in range(1, len(confirmedList)):
        confirmedRow = confirmedList[index]

        country = confirmedRow[1]
        countryData = {}
        if countries.get(country) is None:
            countryData[nameKey] = country

            countryData[startDateKey] = startDate
            countryData[endDateKey] = endDate
            countryData[latKey] = confirmedRow[2]
            countryData[lonKey] = confirmedRow[3]

            countryData[confirmedKey] = parseTimeSeries(confirmedRow)

            countries[country] = countryData
        else:
            mergeTimeSeries(countries[country].get(
                confirmedKey), parseTimeSeries(confirmedRow))

    for index in range(1, len(recoveredList)):
        recoveredRow = recoveredList[index]
        country = recoveredRow[1]
        if(countries.get(country).get(deathsKey) is None):
            countries[country][recoveredKey] = parseTimeSeries(recoveredRow)
        else:
            mergeTimeSeries(countries[country].get(
                recoveredKey), parseTimeSeries(recoveredRow))

    for index in range(1, len(deathList)):
        deathsRow = deathList[index]
        country = deathsRow[1]
        if(countries.get(country).get(deathsKey) is None):
            countries[country][deathsKey] = parseTimeSeries(deathsRow)
        else:
            mergeTimeSeries(countries[country].get(
                deathsKey), parseTimeSeries(deathsRow))

    for countryKey in countries.keys():
        country = countries.get(countryKey)
        country[newConfirmedKey] = getDelta(country.get(confirmedKey))
        country[newDeathsKey] = getDelta(country.get(deathsKey))
        country[newRecoveredKey] = getDelta(country.get(recoveredKey))

        country[percentageConfirmedKey] = getPercentualChange(
            country.get(confirmedKey), country.get(newConfirmedKey))
        country[percentageDeathsKey] = getPercentualChange(
            country.get(deathsKey),  country.get(newDeathsKey))
        country[percentageRecoveredKey] = getPercentualChange(
            country.get(recoveredKey),  country.get(newRecoveredKey))

        country[activeKey] = getActiveCases(country)
        country[newActiveKey] = getDelta(country.get(activeKey))
        country[percentageActiveKey] = getPercentualChange(
            country.get(activeKey), country.get(newActiveKey))

        country[latestActiveKey] = getLastValueSafely(country.get(activeKey))
        country[latestRecoveredKey] = getLastValueSafely(
            country.get(recoveredKey))
        country[latestDeathsKey] = getLastValueSafely(country.get(deathsKey))

    return countries


def getLastValueSafely(list):
    if(len(list) > 0):
        return list[-1]

    return 0


def getNumberSavelyFromList(list, index):
    if(index < len(list)):
        return list[index]

    return 0


def transformSingleList(csvList):
    countries = {}

    defRow = csvList[0]

    lowestRowIndex = 4
    highestRowIndex = len(defRow)-1

    startDate = getDate(defRow[lowestRowIndex])
    endDate = getDate(defRow[highestRowIndex])

    for index in range(1, len(csvList)):
        row = csvList[index]
        country = row[1]
        countryData = {}
        if countries.get(country) is None:
            countryData[startDateKey] = startDate
            countryData[endDateKey] = endDate
            countryData[latKey] = row[2]
            countryData[lonKey] = row[3]
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
    for i in range(len(timeSeries1)):
        if(i < len(timeSeries2)):
            timeSeries1[i] += timeSeries2[i]
    return timeSeries1


def getDelta(list):
    delta = []
    if len(list) != 0:
        delta.append(list[0])

        for index in range(len(list) - 1):
            delta.append(list[index + 1] - list[index])

    return delta


def getActiveCases(country):
    active = []
    confirmedList = country.get(confirmedKey)
    deathList = country.get(deathsKey)
    recoveredList = country.get(recoveredKey)

    for index in range(0, len(confirmedList)):
        active.append(getNumberSavelyFromList(confirmedList, index) -
                      getNumberSavelyFromList(deathList, index) - getNumberSavelyFromList(recoveredList, index))

    return active


def getPercentualChange(cumulatedList, deltaList):
    percent = []

    if len(cumulatedList) != 0 and len(deltaList) != 0:
        for index in range(len(cumulatedList)):
            if index < len(deltaList) and deltaList[index] != 0 and cumulatedList[index] != 0:
                negative = False
                value = deltaList[index]
                if(value < 0):
                    negative = True
                    value = abs(value)
                percentage = value / cumulatedList[index]
                if(negative):
                    percentage *= -1
                percent.append(percentage * 100)
            else:
                percent.append(0)

    return percent
