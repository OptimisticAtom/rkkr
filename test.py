# import time
import os
# https://docs.python.org/3/library/time.html#time.time

# current time in seconds since 1970
# print(time.time())

# convert time in seconds into a readable string of characters
# print(time.ctime(time.time()))


# the hour of the day
# print(time.localtime(time.time()).hour)

file = open('tehfile', 'a')
if(not(os.path.exists('/home/kyle/Documents/Programming/Python/countFile'))):
    countFileNew = open('count', 'w')
    countFileNew.write('0')
    countFileNew.close()


countFile = open('count', 'w+')
count = int(countFile.read())
for i in range(count, count + 10):
    file.write('meme: ' + str(i) + '  ')
    newCount = i
# hi
countFile.write(str(newCount))
countFile.close()
file.close()
