import requests
#import json

def getAlert(s):
    # Add a check to see if it's a real state
    html = requests.get(f'https://api.weather.gov/alerts/active?area={s}').text
    return html

def getForcast():
    html = requests.get(f'https://api.weather.gov/points/{38.256111},{-85.751389}').text
    return html

if __name__ == '__main__':
    #state = str(input("Input State (e.g. WA): "))
    #alert = getAlert(state)
    forcast = getForcast()
    print(forcast)



