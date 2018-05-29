# scrapes weather from weather.com and prints its data

import requests
from bs4 import BeautifulSoup

url = 'https://weather.com/weather/tenday/l/USOK0412:1:US'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "lxml")

#opens lists for weather data
date = []
date_month_day = []
description = []
high_low = []
precip = []
humidity = []
wind = []

#scrapes weather date (day of week)
for stories in soup.find_all(class_="date-time"):
        date.append(stories.text)

#scrapes weather date (month/day)
for stories in soup.find_all(class_="day-detail clearfix"):
        date_month_day.append(stories.text)

#scrapes weather description
for stories in soup.find_all(headers="description"):
        description.append(stories.text)

#scrapes weather high-low
for stories in soup.find_all(headers="hi-lo"):
        high_low.append(stories.text)

#scrapes weather precipitation
for stories in soup.find_all(headers="precip"):
        precip.append(stories.text)

#scrapes weather humidity
for stories in soup.find_all(headers="humidity"):
        humidity.append(stories.text)

#scrapes weather wind
for stories in soup.find_all(headers="wind"):
        wind.append(stories.text)

#prints final forecast
print("======================")       
print("5 Day Weather Forecast")
print("======================")
print(date[0] + ",", date_month_day[0] + " :|:", description[0] + " *", "^" + high_low[0] + " *", precip[0], "Chance of rain" + " *", humidity[0], "Humidity" + " *", "Winds", wind[0])
print(date[1] + ",", date_month_day[1] + " :|:", description[1] + " *", "^" + high_low[1] + " *", precip[1], "Chance of rain" + " *", humidity[1], "Humidity" + " *", "Winds", wind[1])
print(date[2] + ",", date_month_day[2] + " :|:", description[2] + " *", "^" + high_low[2] + " *", precip[2], "Chance of rain" + " *", humidity[2], "Humidity" + " *", "Winds", wind[2])
print(date[3] + ",", date_month_day[3] + " :|:", description[3] + " *", "^" + high_low[3] + " *", precip[3], "Chance of rain" + " *", humidity[3], "Humidity" + " *", "Winds", wind[3])
print(date[4] + ",", date_month_day[4] + " :|:", description[4] + " *", "^" + high_low[4] + " *", precip[4], "Chance of rain" + " *", humidity[4], "Humidity" + " *", "Winds", wind[4])
