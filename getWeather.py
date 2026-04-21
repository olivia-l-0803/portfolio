import openmeteo_requests
import requests
from datetime import datetime

def getTempWeek(): #function for weekly highs and lows
    get = requests.get("https://api.open-meteo.com/v1/forecast?latitude=40.6&longitude=-70.1&daily=temperature_2m_max,temperature_2m_min&hourly=temperature_2m,apparent_temperature&current=temperature_2m&timezone=America%2FNew_York&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch")
    if get.status_code != 200:
        return "Error!!"
        #catches errors in getting the data

    data = get.json()

    Daily =[]

    for i in range(0,7):
        Daily.append((data["daily"]["time"][i], str(data["daily"]["temperature_2m_max"][i]), str(data["daily"]["temperature_2m_min"][i]))) 
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

def getTempHour(): #Hourly Highs and Lows
    get = requests.get("https://api.open-meteo.com/v1/forecast?latitude=40.6&longitude=-70.1&hourly=,temperature_2m,weather_code,apparent_temperature&timezone=America%2FNew_York&past_days=0&forecast_days=7&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch")
    if get.status_code != 200:
        return "Error!!"
        #catches errors in getting the data
    
    data = get.json()

    currentTime = str(datetime.now().hour)
    
    dates = data["hourly"]["time"]

    #this loop finds when to start aka, the current time!!
    for i in range(24):
        if currentTime in dates[i][11:13]:
            currentTimeIndex = i
            break

    #gathering the hourly weather and organizing 
    HourlyTemp = []
    HourlyApp = []
    HourCode= []

    for i in range(24):
        index = i + currentTimeIndex
        HourlyTemp.append(data["hourly"]["temperature_2m"][index])
        HourlyApp.append(data["hourly"]["apparent_temperature"][index])
        HourCode.append(data["hourly"]["weather_code"][index])



    
    


    return HourlyTemp, HourCode, HourCode
    #A tuple will come out
        
    



#getting + interpreting Weather Codes!

def currentWeatherCode():
    get = requests.get("https://api.open-meteo.com/v1/forecast?latitude=40.6&longitude=-70.1&current=weather_code&timezone=America%2FNew_York&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch")
    if get.status_code != 200:
        return "Error."
    data = get.json()
    return data["current"]["weather_code"]

def codeToPicture(code: int): #this will interpret the code to a tuple (image file name, meaning) . Using google noto color emoji for icons
    if code == 0: 
        return "icons/sunny.png", "Clear Sky"
    if code == 1 or code == 2: 
        return "icons/partlyCloudy.png", "Partly Cloudy"
    if code == 3: 
        return "icons/cloudy.png", "Overcast"
    if code == 45 or code == 48:
        return "icons/foggy.png", "Foggy"
    if code in (51, 53, 55):
        return "icons/drizzle.png", "Drizzle"
    if code in (56, 57):
        return "icons/snow.png", "Freezing Drizzle"
    if code in (61, 63, 65):
        return "icons/rainy.png", "Rainy"
    if code in (66, 67):
        return "icons/snow.png", "Freezing Rain"
    if code in (71, 73, 75, 77, 85, 86):
        return "icons/snow.png", "Snow"
    if code in (95, 96, 99):
        return "icons/thunderstorm.png", "Thunderstorm"
    
def getForecastWeek(): #function for the weeks weather codes 
    get = requests.get("https://api.open-meteo.com/v1/forecast?latitude=40.6&longitude=-70.1&daily=weather_code&timezone=America%2FNew_York&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch")
    if get.status_code != 200:
        return "Error!!"
        #catches errors in getting the data

    data = get.json()

    Codes =[]

    for i in range(0,7):
        Codes.append(codeToPicture(data["daily"]["weather_code"][i])) 
    #automatically converting to the image file for easier use!

    return Codes  
    
    

#Testing current temp

curTemp = getCurrentTemp()
print("Current", curTemp )

#testing weekly temp

weekTemp = getTempWeek()
print("Week", weekTemp)

#testing hourly temp
hourTemp = getTempHour()
print("Hour", hourTemp)


#testing the Current Weather icon
curCode = currentWeatherCode()

interpretedCode = codeToPicture(curCode)

print(curCode, interpretedCode[0], interpretedCode[1]) 

print(getForecastWeek()) #testing weekly forecast
weekWeather = getForecastWeek()






