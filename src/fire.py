#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
import sys
from optparse import OptionParser
import os

parser = OptionParser()

parser = OptionParser("usage: %prog [options] ",
    version="%prog 1.0")

rser.add_option("-p", "--port",
    action="store",
    type="string",
    dest="port",
    help="2 digit country identifier")

rser.add_option("-d", "--delay",
    action="store",
    type="string",
    dest="delay",
    default=1,
    help="Time in seconds to delay, default is 1 second")

parser.add_option("--off",
    action="store_true",
    dest="lightsOff")

parser.add_option(
    "--all",
    action="store_true",
    dest="lightsOn")

(opts, args) = parser.parse_args()




relays = [3, 5, 7, 11]

def setup():

#    GPIO.setmode(GPIO.BCM)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(relays, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(tree, GPIO.OUT, initial=GPIO.HIGH)

# Base function to turn relay on, pass it board gpio pin number
def relay_on(relay):
    #print "Relay on " + str(relay)
    GPIO.output(relay, GPIO.LOW)
    
# Base function to turn relay off, pass it board gpio pin number
def relay_off(relay):
    #print "Relay off " + str(relay)
    GPIO.output(relay, GPIO.HIGH)


setup()

parser = OptionParser()
parser.add_option("--off", action="store_true", dest="lightsOff")
parser.add_option("--on", action="store_true", dest="lightsOn")

(opts, args) = parser.parse_args()

