import time
# https://docs.python.org/3/library/time.html#time.time

# current time in seconds since 1970
print(time.time())

# convert time in seconds into a readable string of characters
print(time.ctime(time.time()))


# the hour of the day
print(time.localtime(time.time()).hour)
