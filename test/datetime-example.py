import time

# print (time.gmtime(0))
# print (time.localtime())
# print (time.time())
#
# for i in range(10):
#     print (time.time())
# time_here  = time.localtime()
# print (time_here)
# print("Year:", time_here[0], time_here.tm_year)
# print("Month:", time_here[1], time_here.tm_mon)
# print("Day:", time_here[2], time_here.tm_mday)


#from time import time as my_timer
# from time import perf_counter as my_timer
#
# import random
# input ("press enter to start")
# wait_time = random.randint(1,6)
# time.sleep(wait_time)
# start_time = my_timer()
# input ('press enter to stop')
# end_time = my_timer()
#
# print ("Started at " + time.strftime("%X", time.localtime(start_time)))
# print ("Ended at " + time.strftime("%X", time.localtime(end_time)))
# print ("Your reaction time was {} seconds".format(end_time- start_time))

# print ("The epoch starts at: " + time.strftime("%c", time.gmtime(0)))
# print ("The current timezone is {0} with an offset of {1} hours".format(time.tzname[0], time.timezone/3600))
#
# if time.daylight != 0:
#     print ("\tDaylight savings time is in effect for this location")
#     print ("\tDST timezone is "+time.tzname[1])
#
# print ("Local Time is "+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print ("UTC Time is "+ time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

import datetime
print (datetime.datetime.today())
print (datetime.datetime.now())
print (datetime.datetime.utcnow())