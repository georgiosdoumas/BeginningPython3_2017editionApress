#!/usr/local/bin/python3
import time, random
date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = time.mktime(date1)
print(time1)
date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = time.mktime(date2)
print(time2)
random_time = random.uniform(time1, time2)
print(random_time)
print(time.asctime(time.localtime(random_time)))
 ## Now some examples I crafted :
inpdate = input("Enter a initial date of desired time-period, in format Jan 31 2000 :")
date1 = time.strptime(inpdate, "%b %d %Y")
inpdate = input("Enter final date in the same format : ")
date2 = time.strptime(inpdate, "%b %d %Y")
time1 = time.mktime(date1)
time2 = time.mktime(date2)
random_time = random.uniform(time1, time2)
print("A randon date in this time period is : ", time.asctime(time.localtime(random_time)))

