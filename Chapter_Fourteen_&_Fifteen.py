print('Hello world . . . ')

print('This is the start of the Chapter Fourteen exercises. ' )

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Date:
    """Represents a year, month, and day"""

    def __init__(self):
        self.day = None
        self.month = None
        self.year = None

    def __str__(self):  # Overloading string instead of writing print_date.
        return f'{self.year:4d}-{self.month:02d}-{self.day:02d}'

def make_date(year, month, day):
    date = Date()
    date.year = year
    date.month = month
    date.day = day
    return date

def is_leap_year(date):  # Basic math to determine if this is a leap year.
    return (date.year % 4 == 0 and date.year % 100 != 0) or (date.year % 400 == 0)

def get_days_since_year_start(date):
    days = date.day
    for day_cnt in range(0, date.month - 1):  # month - 1 because the current month is not yet over.
        days += DAYS_IN_MONTH[day_cnt]
        if day_cnt == 1 and is_leap_year(date):  # Got to check if this is a leap year
            days += 1
    return days

def date_to_int(date):
    epoch = make_date( 1970, 1, 1 )
    years = date.year - epoch.year  # Years since epoch
    leap_years = floor(years/4)    # Leap years since epoch
    non_leap_years = years - leap_years  # Non Leap years since epoch
    # LeapYearDays + NonLeapYearDays + MonthDays
    days = (non_leap_years * 365) + (leap_years * 366) + get_days_since_year_start(date)
    return days

def is_date_after(d1, d2):
    return True if date_to_int(d1) > date_to_int(d2) else False

class Time:
    """Represents a time of day."""

    def __init__(self):
        self.second = None
        self.minute = None
        self.hour = None

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    minute, second = divmod(seconds, 60)
    hour, minute = divmod(minute, 60)
    return make_time(hour, minute, second)

def add_time(time, hours, minutes, seconds):
    duration = make_time(hours, minutes, seconds)
    seconds = time_to_int(time) + time_to_int(duration)
    return int_to_time(seconds)



def subtract_time(t1, t2):
    return int_to_time(time_to_int(t2) - time_to_int(t1))


def is_after(t1, t2):
    return True if time_to_int(t1) > time_to_int(t2) else False

def is_after_date(d1, d2):
    return True if (d1.year, d1.month, d1.day) > (d2.year, d2.month, d2.day) else False



def print_date(date):
    print(f"The The ISO 8601 format YYYY-MM-DD | Year, Month, Day is : {date.year}-{date.month}-{date.day}.")



def main():
    print(subtract_time(make_time(11, 30, 58), make_time(23,29, 59)))
    print("-"*120)
    print(is_after(make_time(3,2, 1), make_time(3, 2, 0)))
    print(is_after(make_time(3,2, 1), make_time(3, 2, 1)))
    print(is_after(make_time(11,12, 0), make_time(9, 40, 0)))
    print("-"*120)
    print(make_date(1933, 6, 22))
    print("-"*120)
    print(is_leap_year(make_date(2024, 6, 22)))  # Leap year
    print(is_leap_year(make_date(1900, 6, 22)))  # Not a Leap year
    print(is_leap_year(make_date(1600, 6, 22)))  # Leap year
    print(get_days_since_year_start(make_date(2024, 6, 22)))  # Leap year
    print(get_days_since_year_start(make_date(1933, 6, 22)))  # Not a leap year
    print("-"*120)
    print(date_to_int(make_date(2024, 11,15)))  # 20043 as of 11/15/2024
    print(date_to_int(make_date(2024, 10,15)))  # 20012 as of 10/15/2024
    print("-"*120)
    print(is_date_after(make_date(2024, 11, 15), make_date(2024, 11, 15)))
    print(is_date_after(make_date(2024, 11, 15), make_date(2024, 10, 15)))
    print(is_date_after(make_date(2024, 11, 15), make_date(2024, 12, 15)))





print("-"*120)

print(subtract_time(make_time(7, 30, 57), make_time(7,35, 59)))

print(time_to_int(subtract_time( int_to_time(7000), int_to_time(14000) ) ) )

print("-"*120)

print((is_after( int_to_time(7000), int_to_time(14000) ) ) )
print("-"*120)

print((is_after( int_to_time(14000), int_to_time(7000) ) ) )

print("-"*120)

print(make_date(1933, 6, 22))

print("-"*120)

print_date(make_date(1933, 6, 22))

print("-"*120)

print(is_after_date(make_date(1933, 6, 22), make_date(1933, 9, 17)))

print("-"*120)


print('This is the end of the Chapter Fourteen exercises. ' )

print("-"*120)

print('This is the start of the Chapter Fifteen exercises. ' )




from enum import Enum
from math import floor


class Epoch(Enum):
    year = 1970
    month = 1
    day = 1


class Date:
    # Kind-a equivalent to Java's static final variables.
    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    """Represents a year, month, and day"""

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def is_leap_year(self):  # Basic math to determine if this is a leap year.
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def get_days_since_year_start(self):
        days = self.day
        for day_cnt in range( 0, self.month - 1 ):  # month - 1 because the current month is not yet over.
            days += Date.DAYS_IN_MONTH[day_cnt]
            if day_cnt == 1 and self.is_leap_year():  # Got to check if this is a leap year
                days += 1
        return days

    def date_to_int(self):
        years = self.year - Epoch.year.value  # Years since epoch
        leap_years = floor( years / 4 )  # Leap years since epoch
        non_leap_years = years - leap_years  # Non Leap years since epoch
        # LeapYearDays + NonLeapYearDays + MonthDays
        days = (non_leap_years * 365) + (leap_years * 366) + self.get_days_since_year_start()
        return days

    def is_after(self, d2):
        return True if self.date_to_int() > d2.date_to_int() else False

    def __str__(self):  # Overloading string instead of writing print_date.
        return f'{self.year:4d}-{self.month:02d}-{self.day:02d}'





def main_2():
    d0 = Date(2024, 11, 15)
    d1 = Date(2024, 6, 22)
    d2 = Date(1933, 6, 22)
    d3 = Date(1900, 6, 22)
    d4 = Date(1600, 6, 22)
    print(d1, d2, d3, d4)
    print("-"*120)
    print(d1.is_leap_year())  # Is a Leap Year
    print(d2.is_leap_year())  # Not a Leap Year
    print(d3.is_leap_year())  # Not a Leap Year
    print(d4.is_leap_year())  # Is a Leap Year
    print("-"*120)
    print(d1.get_days_since_year_start())  # Leap Year
    print(d2.get_days_since_year_start())  # Not a Leap Year
    print("-"*120)
    print( Date(2024, 11,15).date_to_int() )  # 20043 as of 11/15/2024
    print( Date(2024, 10,15).date_to_int() )  # 20012 as of 10/15/2024
    print("-"*120)
    print(d0.is_after(Date(2024, 11, 15)))
    print(d0.is_after(d1))
    print(d0.is_after(Date(2024, 12, 15)))


print("-"*120)

print('This is the end of the Chapter Fifteen exercises. ' )