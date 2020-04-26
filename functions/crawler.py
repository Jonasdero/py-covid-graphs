import requests
import csv


def getCSV(csvURL):
    with requests.Session() as s:
        download = s.get(csvURL)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        return my_list
