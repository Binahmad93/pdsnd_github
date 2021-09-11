#importing time, pandas, and numpy
import time
import pandas as pd
import numpy as np

#dictinary of 3 csv files.
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


#get user input about his\her choices to specify a city, month, and day to analyze.
#function to handle user choices.
def get_filters():

    city = input('Would you like to see data for Chicago, New York, or Washington?\n').lower()
    month = input('Enter a month from January to June or type all to view all months \n ').title()
    day = input('Which day you want the data for? or type "all" to view all data\n').title()

#lists of user choices we want to get from.
    cities = ['chicago','new york city','washington']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All']

#just read pyhton as words!
    if city in cities and(month in months and day in days):

#format puts city, month and day the user input above in {} to make user see like city: ... etc
        print('Great You Choose the data for this city: {} in month: {} at day:{}'.format(city, month, day))
    while city not in cities or(month not in months or day not in days):

#print() will print to the output and because of \n the user will see the dialoge in 2 lines.
        print('For now,we only cover these cities please choose from them:\n  chicago, new york city, washington')
        print('Unfortunately, we only have the data for these months, please choose from them:\n    January, February, March, April, May, June, or type "All" to view everything')
        print('I belive you have something wrong, below are week days please choose from them or type "all" to view everyday.\n   Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday')

#.lower() makes all inputs from the user either uppercase or lowercase in lowercase.
#.title() makes all inputs from the user as title first letter capital and the rest of the word is not
        city = input('Would you like to see data for Chicago, New York, or Washington?\n').lower()
        month = input('Enter a month from January to June or type all to view all months \n ').title()
        day = input('Which day you want the data for? or type "all" to view all data\n').title()

        if city in cities and(month in months and day in days):
            print('Great You Choose the data for this city: {}, in month: {}, at day: {}.'.format(city, month, day))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
        Loads data for the specified city and filters by month and day if applicable.
        df = pd.read_csv(CITY_DATA[city])
        Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


#load data from csv file
    df = pd.read_csv(CITY_DATA[city])

#convert column start time to date to extract any date we want
    df['Start Time'] = pd.to_datetime(df['Start Time'])

#make column month from date
    df['month'] = df['Start Time'].dt.month_name()

# the same with day and hour
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'All':

#input month now will appear only on column month
        df = df[df['month'] == month]
    if day != 'All':


#day too
        df = df[df['day'] == day]
    print('-'*40)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

# TO DO: display the most common month
    print('The common month: \n', df['month'].mode()[0])


# TO DO: display the most common day
    print('The common day: \n', df['day'].mode()[0])


# TO DO: display the most common start hour
    print('The common hour: \n', df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


# TO DO: display most commonly used start station
    print('The common starting station is:\n', df['Start Station'].mode()[0])


# TO DO: display most commonly used end station
    print('The common ending station is\n', df['End Station'].mode()[0])


# TO DO: display most frequent combination of start station and end station trip
    df['frequent'] = df['Start Station'] + ' AND ' + df['End Station']
    print('The common_frequent_station\n', df['frequent'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


# TO DO: display total travel time
    print('Total travel time in seconds\n', df['Trip Duration'].sum())
    print('Total travel time in hours\n', (df['Trip Duration'].sum())/3600)


# TO DO: display mean travel time
    print('Average Time in seconds\n', df['Trip Duration'].mean())
    print('Average Time in hours\n', (df['Trip Duration'].mean())/3600)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()


#Display counts of user tupe
    print('User Types:\n', df['User Type'].value_counts())

#gender
    if 'Gender' in df:
        print('gender counts:\n', df['Gender'].value_counts())


#all description of birth year like max, min, 25%, 50%, 75%
    if 'Birth Year' in df:
        print("description of birth year\n", df['Birth Year'].describe())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def explore(df):


#Determine rows the user want to read
    read = input("How many rows you want us to display?")
    read_0 = int(read)
    print (df[0:read_0])
    again = input("Do you want to explore more rows? (yes or no)\n").lower()
    y = 0

    while True:
        if again != 'yes':
            break
        x = read_0 + y
        read = input("How many rows you want?\n")
        read_1 = int(read)
        y += read_1
        repeated = read_0 + y

        print(df[x:repeated])

        again = input("Do you want to explore more rows? (yes or no)\n").lower()


    print("Thank you for exploring this data")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        explore(df)

        restart = input('\nWould you like to restart? (yes or no)\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
