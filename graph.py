import matplotlib.pyplot as plt
from date import daterange


def showCountryPlot(countryCases, countryDeaths, countryRecovered, country):

    startDate = countryCases.get(country).get('startDate')
    endDate = countryCases.get(country).get('endDate')

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
    plt.title(country + " (" + countryCases.get(country).get("lat") +
              ", " + countryCases.get(country).get("long") + ")")

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()


def showPlot(countryDic, countries, title):
    startDate = countryDic.get(countries[0]).get('startDate')
    endDate = countryDic.get(countries[0]).get('endDate')

    # x axis values
    x = list(daterange(startDate, endDate))

    for country in countries:
        # corresponding y axis values
        y = countryDic.get(country).get('timeSeries')

        # plotting the points
        plt.plot(x, y, label=country)

    # naming the x axis
    plt.xlabel('Date')
    plt.ylabel('Values')

    # giving a title to my graph
    plt.title(title)

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()
