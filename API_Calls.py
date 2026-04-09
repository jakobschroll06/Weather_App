import requests

headers = {
    'User-Agent': 'jakobschroll06@gmail.com'
}

def getAlerts(s: str):
    url = (f'https://api.weather.gov/alerts/active?area={s}')
    try :
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data.get("features", [])

        else:
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []


def getForcast(lat, lon):
    url = (f'https://api.weather.gov/gridpoints/{"LMK"}/{lat},{lon}/forecast')
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:

            data = response.json()
            return data["properties"]["periods"]
        else:
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []
