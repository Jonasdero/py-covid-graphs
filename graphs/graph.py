import matplotlib.pyplot as plt
from functions.date import daterange
from constantData.keys import confirmedKey, deathsKey, endDateKey, latKey, lonKey, newConfirmedKey, newDeathsKey, newRecoveredKey, recoveredKey, startDateKey, percentageConfirmedKey, percentageDeathsKey, percentageRecoveredKey, activeKey, newActiveKey, percentageActiveKey, nameKey, latestActiveKey, latestDeathsKey, latestRecoveredKey
from scipy.ndimage.filters import gaussian_filter1d


def showCountryPlot(countryCases, countryDeaths, countryRecovered, country):

    startDate = countryCases.get(country).get(startDateKey)
    endDate = countryCases.get(country).get(endDateKey)

    # x axis values
    x = list(daterange(startDate, endDate))
    # corresponding y axis values
    countryCasesY = countryCases.get(country).get('timeSeries')
    countryDeathsY = countryDeaths.get(country).get('timeSeries')
    countryRecoveredY = countryRecovered.get(country).get('timeSeries')

    # plotting the points
    plt.plot(x, countryCasesY, label="Confirmed Cases in " + country)
    plt.plot(x, countryDeathsY, label="Deaths in " + country)
    plt.plot(x, countryRecoveredY, label="Recovered in " + country)

    # naming the x axis
    plt.xlabel('Date')
    plt.ylabel('Values')

    # giving a title to my graph
    plt.title(country + " (" + countryCases.get(country).get(latKey) +
              ", " + countryCases.get(country).get(lonKey) + ")")

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()


def showPlot(countryDic, countries, title):
    startDate = countryDic.get(countries[0]).get(startDateKey)
    endDate = countryDic.get(countries[0]).get(endDateKey)

    # x axis values
    x = list(daterange(startDate, endDate))

    for country in countries:
        # corresponding y axis values
        y = countryDic.get(country).get('timeSeries')

        # plotting the points
        plt.plot(x, y, label=country)

    # naming the axis
    plt.xlabel('Date')
    plt.ylabel('Values')

    # giving a title to my graph
    plt.title(title)

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()


def cumulatedView(country):
    endDate = country.get(endDateKey)
    dateList = list(daterange(
        country.get(startDateKey),
        endDate))

    # https://matplotlib.org/gallery/api/two_scales.html
    fig, ax1 = plt.subplots()
    # naming the axis
    # todo color?
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Active Cases %-Change')
    ax1.plot(dateList,
             filter(country, percentageActiveKey),
             label='Active Cases %-Change', color='black')

    ax2 = ax1.twinx()

    ax2.set_ylabel('Cumulative Cases')
    ax2.plot(dateList, filter(country, activeKey),
             label='Active Cases (' + str(country.get(latestActiveKey)) + ')')
    ax2.plot(dateList,  filter(country, recoveredKey),
             label='Recovered Cases (' +
             str(country.get(latestRecoveredKey)) + ')')
    ax2.plot(dateList, filter(country, deathsKey),
             label='Dead Cases (' + str(country.get(latestDeathsKey)) + ')')

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.title('Cumulated View ' +
              country.get(nameKey) + ' as of ' +
              endDate.strftime('%Y-%m-%d'))
    plt.legend()
    plt.show()


def dailyView(country):
    endDate = country.get(endDateKey)
    dateList = list(daterange(
        country.get(startDateKey),
        endDate))

    # https://matplotlib.org/gallery/api/two_scales.html
    fig, ax1 = plt.subplots()
    # naming the axis
    # todo color?
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Daily new active cases / recoveries')
    ax1.plot(dateList,
             filter(country, newActiveKey),
             label='New Cases')
    ax1.plot(dateList,
             filter(country, newRecoveredKey),
             label='New Recoveries')

    ax2 = ax1.twinx()

    ax2.set_ylabel('Daily new deaths')
    ax2.plot(dateList,  filter(country, newDeathsKey),
             label='New Deaths', color='tab:red')

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.title('Daily View - ' +
              country.get(nameKey))
    plt.legend()
    plt.show()


def filter(country, key):
    return gaussian_filter1d(country.get(key), sigma=2)
