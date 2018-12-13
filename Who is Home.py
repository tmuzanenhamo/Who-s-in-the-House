#!/usr/bin/python

import bluetooth
import time

print ("The purpose of this program is to check who is home")

while True:
      #Get the date and time 
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

    result = bluetooth.lookup_name('B4:C0:F5:B6:0F:99', timeout=2)#toogle scanning of the device given
    if (result != None):
        print "Tawanda is in  the house"
    else:
        print "Tawanda is not in the house"

    result = bluetooth.lookup_name('B0:35:0B:1C:D3:49', timeout=2)
    if (result != None):
        print "Belie is in the house"
    else:
        print "Belie is not in the house"

    time.sleep(60)

