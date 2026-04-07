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


def getForcast():
    #url = (f'https://api.weather.gov/points/{38.256111},{-85.751389}')
    url = (f'https://api.weather.gov/gridpoints/{"LMK"}/{50},{78}/forecast')
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response = response.json()
        response = json.dumps(response, indent=2)
        print(response)
    else:
        print(f"Error: {response.status_code}")

if __name__ == '__main__':

    state = str(input("Input State (e.g. WA): "))
    getAlerts(state)
    print("------------------------------")
    getForcast()






