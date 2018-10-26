# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz
import random

tzlist = pytz.all_timezones
# print (tzlist)
# print (type (tzlist))
# print (len(pytz.all_timezones))

choice = list()
choice.insert(0, "Quit")

for i in range (1,10):
    n = random.randint(1,len(pytz.all_timezones))
#    print ("selecting tz # {} {}".fsormat(n,pytz.all_timezones[n]))
    choice.append( pytz.all_timezones[n])

done = False
while not done:
    for i in range(0,len(choice)):
        print ("{} -- {}".format(i,choice[i]))
    try:
        userInput = input("choose a number:  ")
        sel = int(userInput)
        #print (type (sel))
        if sel == 0:
            done = True
        elif (sel >= 10):
            print ("invalid entry!")
        else:
            print ( "you selected {}   {}".format(sel, choice[sel]))
            local_time =datetime.datetime.now()
            utc_time = datetime.datetime.utcnow()

            print (local_time, local_time.tzinfo)
            tz = pytz.timezone(choice[sel])
            t1 = datetime.datetime.now(tz=tz)
#            print ( 'choosing tz: ', tz)
#            t1 = pytz.utc.localize(local_time).astimezone(tz)

            print()
            print ("-"*40)
            print("Time is {} in {}".format(t1, tz))
            print("Local Time is {}".format(local_time))
            print("UTC Time is {}".format(utc_time))
            print ("-"*40)

            #t1 = local_time.tzinfo
            #print (t1)
    except:
        print ("invalid entry")
        pass


#for tz in pytz.