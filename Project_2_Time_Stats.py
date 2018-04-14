# Project 2 : Time Stats 
import time
import pandas as pd
import numpy as np


chicago=pd.read_csv('chicago.csv')
new_york_city = pd.read_csv('new_york_city.csv')
washington = pd.read_csv('washington.csv')

def time_stats(chicago):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    # start_time = time.time()
    chicago['Start Time'] = pd.to_datetime(chicago['Start Time'])
    # display the most common month

   
    chicago['Month'] = chicago['Start Time'].dt.strftime('%B')
    # display the most common day of week
    chicago['Day'] = chicago['Start Time'].dt.weekday

    # display the most common start hour
    chicago['HR'] = chicago['Start Time'].dt.hour 

    print(chicago.groupby(['Month']).size())
    print(chicago.groupby(['Day']).size())
    print(chicago.groupby(['HR']).size())
    #print("\nThis took %s seconds." % (time.time() - start_time))
    #print('-'*40)
