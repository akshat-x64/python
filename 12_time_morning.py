# importing datetime module
from datetime import datetime

# now is a method in datetime module is
# used to retrieve current data,time
myobj = datetime.now()

# printing current hour using hour
# class
print("Current hour ", myobj.hour)

# printing current minute using minute
# class
print("Current minute ", myobj.minute)

# printing current second using second
# class
print("Current second ", myobj.second)

# printing current microsecond using
# microsecond class
print("Current microsecond ", myobj.microsecond)
hour = myobj.hour
if (hour >= 5 and hour < 12):
    print("Goodmoring")
elif (hour >= 12 and hour < 17):
    print("Goodafternoon")
elif (hour >= 17 and hour <= 21):
    print("Goodevening")

print(type(hour))
