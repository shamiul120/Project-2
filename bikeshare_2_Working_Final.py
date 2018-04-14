
import pandas as pd
import numpy as np



chicago=pd.read_csv('chicago.csv')
new_york_city = pd.read_csv('new_york_city.csv')
washington = pd.read_csv('washington.csv')
                    
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
def get_city_name():    
    while True:
        city_name = input("\nHello! Let\'s explore some US bikeshare data!\n"
                     "Please select the city name (Chicago, New York, or Washington) :\n").lower().replace(' ', '_')
        if city_name == "chicago" or city_name == "newyork" or city_name == "washington":
            #print(city_name)
             return (city_name)
            
def get_month_name():
    while True:
        month_name = input("\nPlease select the Month (January, February, March, April, May, or June) :\n").lower().replace(' ', '_')
        if month_name == "january" or month_name == "february" or month_name == "march" or month_name == "april" or month_name == "may" or month_name == "june":
            #print(month_name)
            return(month_name)

def get_day_name():
    while True:
        day_name = input('\nPlease select the Day ( Friday, Saturday, Subday, Monday, Tuesday, Wednesday, Thursday) :\n').lower().replace(' ', '_')
        if day_name == "friday" or day_name == "saturday" or day_name == "sunday" or day_name == "monday" or day_name == "tuesday" or day_name == "wednesday" or day_name == "thursday":
            #print(day_name)
            return(day_name)

            #print('_'*40)
            #return(city_name, month_name, day_name)



chicago = pd.read_csv('C:\Python\!Project_2/chicago.csv')

chicago['Start Time'] = pd.to_datetime(chicago['Start Time'])

chicago['Year'] = chicago['Start Time'].dt.strftime('%Y')

chicago['Month'] = chicago['Start Time'].dt.strftime('%B')

chicago['Day'] = chicago['Start Time'].dt.strftime('%A')

chicago['HR'] = chicago['Start Time'].dt.hour 


print(chicago.groupby(['Year']).size())
print(chicago.groupby(['Month']).size())
print(chicago.groupby(['Day']).size())
print(chicago.groupby(['HR']).size())

#print(max(max_month).size())



   
