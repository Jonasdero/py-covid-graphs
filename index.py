from constantData.urls import confirmedGlobalUrl, deathsGlobalUrl, recoveredGlobalUrl
from functions.crawler import getCSV
from functions.parser import parseData
from graphs.graph import cumulatedView, dailyView

countriesList = parseData(getCSV(confirmedGlobalUrl), getCSV(
    deathsGlobalUrl), getCSV(recoveredGlobalUrl))

country = 'US'
# print(countriesList.get('Germany'))
cumulatedView(countriesList.get(country))
dailyView(countriesList.get(country))
