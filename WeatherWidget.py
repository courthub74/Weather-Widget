from tkinter import *
import pandas as pd 
import requests
from bs4 import BeautifulSoup
from time import sleep

#take straight from the URL
page = requests.get('https://forecast.weather.gov/MapClick.php?textField1=42.48&textField2=-83.36')
#https://forecast.weather.gov/MapClick.php?lat=34.09927000000005&lon=-118.338069999999996#.XIRJ81NKgUE
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id= 'seven-day-forecast-body')

items = week.find_all(class_ = 'tombstone-container')

#the GUI
root = Tk()
theLabel = Label(root, text="Your Weekly Forecast", width=30, font="none 30 bold", fg="blue")
theLabel.pack() 

#the BACKGROUND
root.configure(background="Blue")

#the FORECAST output
theForecast = Text(root, width = 30, font="none 15", wrap=WORD, background="white")
theForecast.pack()


#POINT
point = '*'

#DAY1
day1name = items[0].find(class_ = "period-name").get_text()
day1cast = items[0].find(class_ = "short-desc").get_text()
day1temp = items[0].find(class_ = "temp").get_text()


#DAY2
day2name = items[1].find(class_ = "period-name").get_text()
day2cast = items[1].find(class_ = "short-desc").get_text()
day2temp = items[1].find(class_ = "temp").get_text()

#DAY3
day3name = items[2].find(class_ = "period-name").get_text()
day3cast = items[2].find(class_ = "short-desc").get_text()
day3temp = items[2].find(class_ = "temp").get_text()

#DAY4
day4name = items[3].find(class_ = "period-name").get_text()
day4cast = items[3].find(class_ = "short-desc").get_text()
day4temp = items[3].find(class_ = "temp").get_text()

#DAY5
day5name = items[4].find(class_ = "period-name").get_text()
day5cast = items[4].find(class_ = "short-desc").get_text()
day5temp = items[4].find(class_ = "temp").get_text()

#DAY6
day6name = items[5].find(class_ = "period-name").get_text()
day6cast = items[5].find(class_ = "short-desc").get_text()
day6temp = items[5].find(class_ = "temp").get_text()

#DAY7
day7name = items[6].find(class_ = "period-name").get_text()
day7cast = items[6].find(class_ = "short-desc").get_text()
day7temp = items[6].find(class_ = "temp").get_text()

#DAY8
day8name = items[7].find(class_ = "period-name").get_text()
day8cast = items[7].find(class_ = "short-desc").get_text()
day8temp = items[7].find(class_ = "temp").get_text()

#DAY9
day9name = items[8].find(class_ = "period-name").get_text()
day9cast = items[8].find(class_ = "short-desc").get_text()
day9temp = items[8].find(class_ = "temp").get_text()


#SPACING
spacing1 = '                                                       '

#THE OUTPUT
day1 = [point, day1name, day1cast, day1temp]
theForecast.insert(0.0, day1)

theForecast.insert(2.5,spacing1)

day2 = [point, day2name, day2cast, day2temp]
theForecast.insert(5.0, day1)

theForecast.insert(6.0,spacing1)

day3 = [point, day3name, day3cast, day3temp]
theForecast.insert(7.0,day3)

theForecast.insert(8.0,spacing1)

day4 = [point, day4name, day4cast, day4temp]
theForecast.insert(9.0,day4)

theForecast.insert(10.0,spacing1)

day5 = [point, day5name, day5cast, day5temp]
theForecast.insert(11.0,day5)

theForecast.insert(12.0,spacing1)

day6 = [point, day6name, day6cast, day6temp]
theForecast.insert(13.0,day6)

theForecast.insert(14.0,spacing1)

day7 = [point, day7name, day7cast, day7temp]
theForecast.insert(15.0,day7)

theForecast.insert(16.0,spacing1)

day8 = [point, day8name, day8cast, day8temp]
theForecast.insert(17.0,day8)

theForecast.insert(18.0,spacing1)

day9 = [point, day9name]
day92 = [day9cast, day9temp]
theForecast.insert(19.0,day9)
theForecast.insert(20.0,day92)


#MAINLOOP(Anchor)
root.mainloop()
