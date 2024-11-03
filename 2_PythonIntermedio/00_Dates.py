# Dates

from datetime import datetime, time, date, timedelta

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    #timestamp = date.timestamp()
    print(date.timestamp())

print_date(now)

my_date = datetime(2024, 3, 18)

print_date(my_date)

current_time = time(23, 6, 00)

print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

#current_date = date(2024, 3, 18)
current_date = date.today()
print(current_date)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date)

print(my_date - now)
print(my_date.date() - current_date)

start_time_delta = timedelta(200, 100, 100, weeks=10)
end_time_delta = timedelta(200, 100, 100, weeks=13)
print(end_time_delta - start_time_delta)
print(end_time_delta + start_time_delta)
