
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
from tabulate import tabulate


def getpage(url):
    try:
        page = urlopen(url)
    except HTTPError as e:
        return None
    
    return page
    
    
def calc_weather(days , dates , conditions , maxTemps ,minTemps , summary):
    weathers = []
    for i in range(5):
        weather=[]
        weather.append(days[i])
        weather.append(dates[i])
        weather.append(conditions[i])
        weather.append(maxTemps[i])
        weather.append(minTemps[i])
        weather.append(summary[i])
        weathers.append(weather)  
        
    return weathers  
    
def extract_data(bsObj ,days , dates , conditions , maxTemps ,minTemps , summary):
    tables = bsObj.find_all(class_ = "Forecast7Day")
    table = tables[0]

    forecast15days = table.find_all(class_ = "forecastBox")

    for forecast in forecast15days:
        box = forecast.find(class_="fcBox")
    
        heading = box.find(class_ ="forecastHeading")
    
        day = heading.string
        days.append(day)
    
        dateBox = box.find(class_ = "fcDate")
        date = dateBox.string
        dates.append(date)
    
        conditionBox = box.find(class_ = "fcConditionText")
        condition = conditionBox.string
        conditions.append(condition)
    
        tempBox= box.find(class_ = "fcTemperature")
    
        maxTempBox = tempBox.find(class_ = "maxt")
        cmaxBox = maxTempBox.find(class_ ="c")
        maxTemps.append(cmaxBox.string)
    
        minTempBox = tempBox.find(class_ = "mint")
        cminBox = minTempBox.find(class_ ="c")
        minTemps.append(cminBox.string)
    
        cond = forecast.find(class_="WeatherCondition")
        summary.append(cond.string) 
        
def printTable(weathers):
    print(tabulate( weathers , headers=["DAY" ,"Date" ,"Condition" , "Max temp" , "Min temp" , "Summary"]))                       
    

days=[]
dates=[]
conditions = []
temperatures = []
maxTemps = []
minTemps=[]
summary=[]



page = getpage("https://www.skymetweather.com/forecast/weather/india/karnataka/bangalore%20urban/bengaluru/extended-forecast/")

if page==None:
    print("Error reading page")
    
html = page.read()
bsObj = bs(html , "lxml")

#print(bsObj.prettify())

extract_data(bsObj ,days , dates , conditions , maxTemps , minTemps , summary) 
weathers = calc_weather(days , dates , conditions , maxTemps ,minTemps , summary)    
        
printTable(weathers)
     
    
    
    
    
    
    
    
    
    
   
    
    
    
    
    
    
    
    






