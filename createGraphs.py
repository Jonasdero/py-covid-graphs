from constantData.urls import confirmedGlobalUrl, confirmedUSUrl, deathsGlobalUrl, deathsUSUrl, recoveredGlobalUrl
from functions.parser import transformSingleList
from functions.crawler import getCSV
from graphs.graph import showCountryPlot, showPlot

confirmedGlobal = transformSingleList(getCSV(confirmedGlobalUrl))
deathsGlobal = transformSingleList(getCSV(deathsGlobalUrl))
recoveredGlobal = transformSingleList(getCSV(recoveredGlobalUrl))

interestingCountries = ['China', 'Germany',
                        'US', 'United Kingdom', 'Italy', 'France']

showCountryPlot(confirmedGlobal, deathsGlobal, recoveredGlobal, 'China')


# showPlot(confirmedGlobal, interestingCountries, 'Confirmed Cases')
# showPlot(deathsGlobal, interestingCountries, 'Deaths')
# showPlot(recoveredGlobal, interestingCountries, 'Recovered')
