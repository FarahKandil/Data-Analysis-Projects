import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
           
    while True:
        try:
            city=input("Please enter a city to view data:chicago or new york city or washington ")
            city=city.lower()
            if(city=='chicago' or city=='new york city' or city=='washington'):
                break
        except Exception as e:
            print("Input not valid")
           
          
    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        try:
            month=input("For which month would you like to view data: January, Febraury, March, April, May or June. Type 'all' if you want all months.")
            month=month.lower()
            if(month=='january' or month=='february' or month=='march' or month=='april' or month=='may'or month=='june' or month=='all'):
                break
        except Exception as e:
            print("Input not valid")
    
             
       
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day=input("Which day: monday, tuesday, wednesday, thursday, friday, saturday or sunday. Type 'all' if you want all days.")
            day=day.lower()
            if(day=='sunday' or day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday'or day=='friday' or day=='saturday' or day=='all'):
                break
        except Exception as e:
            print("Input not valid")
    
    
            
  
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    
        df = df[df['month'] == month]

    
    if day != 'all':
       
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    
    df['month']=df['Start Time'].dt.month
    popular_month=df['month'].mode()[0]
    print("Most common month: ",popular_month)
    
    # TO DO: display the most common day of week
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day=df['day_of_week'].mode()[0]
    print("Most common day: ",popular_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most common hour: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    popular_startstation=df['Start Station'].mode()[0]
    print("Most popular start station: ",popular_startstation)
    
    # TO DO: display most commonly used end station
    
    popular_endstation=df['End Station'].mode()[0]
    print("Most popular end station: ",popular_endstation)
    
    # TO DO: display most frequent combination of start station and end station trip
    
    combination=(df['Start Station']+df['End Station']).mode()[0]
    print("Most frequent combination of start station and end station trip: ",combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
   
    sum_traveltime=df['Trip Duration'].sum()
    print("Total travel time: ",sum_traveltime)
    
    # TO DO: display mean travel time
    
    mean_traveltime=df['Trip Duration'].mean()
    print("Mean travel time: ",mean_traveltime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print("Counts of user types: ",user_types)
    
    # TO DO: Display counts of gender
    
   
    try:
        gender_count=df['Gender']=df['Gender'].value_counts()
        print("Counts of user types: ",gender_count)
    except:
        print("Gender field not found in Washington file")
        
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest=df['Birth Year'].min()
        print("Earliest year of birth: ",earliest)
        
        recent=df['Birth Year'].max()
        print("Recent year of birth: ",recent)
        
        common=df['Birth Year'].mode()[0]
        print("Common year of birth: ",common)
        
    except:
        print('Birth Year field not found in Washington file')
    
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        response=input("Would you like to view rows of raw data? Yes or No")
        for i,j in df.iterrows():
            print(i,j)
            response=input("Would you like to view more rows of raw data? Yes or No.")
            if(response.lower()!='yes'):
                break
                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
