import openmeteo_requests
import requests

def getTempWeek(): #function for weekly highs and lows
    get = requests.get("https://api.open-meteo.com/v1/forecast?latitude=40.6&longitude=-70.1&daily=temperature_2m_max,temperature_2m_min&hourly=temperature_2m,apparent_temperature&current=temperature_2m&timezone=America%2FNew_York&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch")
    if get.status_code != 200:
        return "Error!!"
        #catches errors in getting the data

    data = get.json()

    Daily =[]

    for i in range(0,7):
        Daily.append((data["daily"]["time"][i], data["daily"]["temperature_2m_max"][i], data["daily"]["temperature_2m_min"][i])) 
    #tuple content: Date, Max, Min
    #Organizing temperatures by days after

    return Daily

def getCurrentTemp(): #Current temperature is here
    get = requests.get("https://api.open-meteo.com/v1/forecast?latitude=40.6&longitude=-70.1&daily=temperature_2m_max,temperature_2m_min&hourly=temperature_2m,apparent_temperature&current=temperature_2m&timezone=America%2FNew_York&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch")
    if get.status_code != 200:
        return "Error!!"
        #catches errors in getting the data

    data = get.json()

    return {"Current Temperature": str(data["current"]["temperature_2m"]) + data["current_units"]["temperature_2m"],
            "Apparent Temperature": str(data["current"]["temperature_2m"]) + data["current_units"]["temperature_2m"]}
    


#Testing this

curTemp = getCurrentTemp()
weekTemp = getTempWeek()
print(curTemp, weekTemp)

print(weekTemp[0][0])