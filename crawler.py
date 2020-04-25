from urls import confirmedGlobalUrl, confirmedUSUrl, deathsGlobalUrl, deathsUSUrl, recoveredGlobalUrl
from functions import getCSV, transformCountries
from graph import showCountryPlot, showPlot

confirmedGlobal = transformCountries(getCSV(confirmedGlobalUrl))
deathsGlobal = transformCountries(getCSV(deathsGlobalUrl))
recoveredGlobal = transformCountries(getCSV(recoveredGlobalUrl))

interestingCountries = ['China', 'Germany',
                        'US', 'United Kingdom', 'Italy', 'France']

# showCountryPlot(confirmedGlobal, deathsGlobal, recoveredGlobal, 'China')


showPlot(confirmedGlobal, interestingCountries, 'Confirmed Cases')
showPlot(deathsGlobal, interestingCountries, 'Deaths')
showPlot(recoveredGlobal, interestingCountries, 'Recovered')
