# The Date & Time
# What are Tick Intervals
# Time intervals are floating-point numbers in units of seconds. Particular instants in time are expressed in seconds since 12:00am, January 1, 1970.(epoch=a particular period of time in history or a person's life.).

# What is Epoch?
# Sounds: ee·pok (British), eh·puhk (American)


# In Python, the epoch is a reference point in time from which time is measured. It's the moment when time "begins" for a particular system or standard.

# Think of it like the zero point on a number line.

# The most commonly used epoch in Python (and many other systems) is:

# January 1, 1970, 00:00:00 (UTC)

# Why is there an epoch?
# Consistent Timekeeping: Using a fixed point in the past allows computers and systems to calculate and compare time in a standardized way, regardless of when the system was built or where it's located.

# Simplified Calculations: It's easier to perform calculations with a single number representing the seconds (or milliseconds, etc.) that have passed since a fixed point, rather than dealing with complex date and time formats.

# How is the epoch used in Python?
# Python's time module provides functions to work with time based on the epoch:

# time.time(): Returns the current time as a floating-point number of seconds since the epoch.
# time.gmtime(seconds): Converts seconds since the epoch to a time tuple in Coordinated Universal Time (UTC).
# time.localtime(seconds): Converts seconds since the epoch to a time tuple in local time.


import calendar
import datetime
import time


ticks = time.time()
ticks2 = time.gmtime(ticks)
ticks3 = time.localtime(ticks)
print("Ticks since 12:00am, January 1, 1970:", ticks)
print(ticks2)
print(ticks3)

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)



cal = calendar.month(2025, 1)
print ("Here is the calendar:")
print (cal)



# date1 = date(2023, 4, 19)
# print("Date:", date1)
# date2 = date(2023, 4, 30)
# print("Date2:", date2)





x = datetime.datetime.now() #The date contains year, month, day, hour, minute, second, and microsecond.
print(x)