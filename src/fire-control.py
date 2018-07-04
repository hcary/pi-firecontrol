#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
import sys
from optparse import OptionParser
import os

parser = OptionParser()

parser = OptionParser("usage: %prog [options] ",
    version="%prog 1.0")

parser.add_option("-p", "--port",
    action="store",
    type="string",
    dest="port",
    default=0,
    help="2 digit country identifier")

parser.add_option("-d", "--delay",
    action="store",
    type="string",
    dest="delay",
    default=1,
    help="Time in seconds to delay, default is 1 second")

parser.add_option("--off",
    action="store_true",
    dest="all_off")

parser.add_option("--all",
    action="store_true",
    dest="all_fire")

(opts, args) = parser.parse_args()


#relays = [29, 31, 33, 35]
relays = [29, 31, 33]
#relays = [29, 29, 31, 33, 35]
#relays = []
#relays.insert(1, 29)
#relays.insert(2, 31)
#relays.insert(3, 33)
#relays.insert(4, 35)
#relays[1] = 11
#relays[2] = 13
#relays[3] = 15
#relays[4] = 19

def setup():

#    GPIO.setmode(GPIO.BCM)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(relays, GPIO.OUT, initial=GPIO.HIGH)

# Base function to turn relay on, pass it board gpio pin number
def relay_on(relay):
    print "Relay on " + str(relay)
    GPIO.output(relay, GPIO.HIGH)
    
# Base function to turn relay off, pass it board gpio pin number
def relay_off(relay):
    print "Relay off " + str(relay)
    GPIO.output(relay, GPIO.LOW)


setup()



for port in relays:
	relay_off(port)

if opts.port == 0:
	exit()

ports = opts.port.split(",")
delay = opts.delay

print ports[0]
            
            
for port in ports:
    port = int(port) - 1
    print "Port: ", port
    relay_on(relays[port])
    sleep(delay)

sleep(2)

for port in relays:
	relay_off(port)

