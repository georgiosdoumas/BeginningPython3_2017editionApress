#!/usr/local/bin/python3

import time

print("The time now that this command is executed is: ", time.asctime())          # e.g. Sun Dec 22 00:56:23 2019
secs = 5
print("We will give you ", secs, " to relax!")
time.sleep(secs)
secs_since_epoch = time.time()
print(secs_since_epoch , " secs have passed since the nominal creation of Unix")  # e.g. 1576972588.2624755
unix_creation_time = time.localtime(0)
print("that is considered to be \n", unix_creation_time)
   # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=1, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
print("What? This format was ungly? ok we can do better")
unixct_pretty = time.asctime(unix_creation_time)
print("So unix was created at : ", unixct_pretty)                                # Thu Jan  1 01:00:00 1970

''' Output:
The time now that this command is executed is:  Sun Dec 22 00:56:23 2019
We will give you  5  to relax!
1576972588.2624755  secs have passed since the nominal creation of Unix
that is considered to be 
 time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=1, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
What? This format was ungly? ok we can do better
So unix was created at :  Thu Jan  1 01:00:00 1970
'''
