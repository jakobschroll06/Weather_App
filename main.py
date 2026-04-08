import json
import requests

headers = {
    'User-Agent': 'jakobschroll06@gmail.com'
}

def getAlerts(s: str):
    url = (f'https://api.weather.gov/alerts/active?area={s}')
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response = response.json()

        for x in response['features']:

            print(x["properties"]["event"])
            print(x["properties"]["description"])
            print("---------------------------------------------")
    else:
        print(f"Error: {response.status_code}")


def getForcast(lat, lon):
    url = (f'https://api.weather.gov/gridpoints/{"LMK"}/{lat},{lon}/forecast')
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()


        ##### data["properties"]['periods'] will have most of the info I am looking for. #####

        # for x in data["properties"]['periods']:
        #     print(x)

        for i in range(len(data["properties"]['periods'])):
            print(data["properties"]["periods"][i]["name"])
            print(data["properties"]['periods'][i]["temperature"], data["properties"]['periods'][i]["temperatureUnit"])
            print(data["properties"]["periods"][i]["detailedForecast"])
            print("-" * 200)

    else:
        print(f"Error: {response.status_code}")

if __name__ == '__main__':

    #state = str(input("Input State (e.g. WA): "))
    #getAlerts(state)
    # print("-" * 20)

    getForcast(50, 78)






