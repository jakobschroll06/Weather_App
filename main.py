import json
import requests

headers = {
    'User-Agent': 'jakobschroll06@gmail.com'
}

def getAlerts(s: str):
    url = (f'https://api.weather.gov/alerts/active?area={s}')
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if len(data['features']) == 0:
            print("No warnings")
            return

        for x in data['features']:

            print(x["properties"]["event"])
            print(x["properties"]["description"])
            print("-" * 200)
    else:
        print(f"Error: {response.status_code}")


def getForcast(lat, lon):
    url = (f'https://api.weather.gov/gridpoints/{"LMK"}/{lat},{lon}/forecast')
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for i in range(len(data["properties"]['periods'])):
            print(data["properties"]["periods"][i]["name"])
            print(f"Temperature: {data["properties"]['periods'][i]["temperature"]}{data["properties"]['periods'][i]["temperatureUnit"]}")
            print(data["properties"]["periods"][i]["detailedForecast"])
            print(f"Wind Speed: {data["properties"]["periods"][i]["windSpeed"]}")
            print("-" * 200)

    else:
        print(f"Error: {response.status_code}")

if __name__ == '__main__':

    # state = str(input("Input State (e.g. WA): "))
    state = "KY"
    getAlerts(state)
    print("#" * 200)

    getForcast(50, 78)






