#!/usr/bin/env python2.7

## OSC2Telnet ##
## v0.02 ##
## gllmar 2015 ##

from OSC import OSCServer,OSCClient, OSCMessage
import sys
from time import sleep
import types

import argparse
import getpass
import telnetlib


# gestion des arguments
parser = argparse.ArgumentParser(description='OSC2Telnet')

#parser.add_argument('-o','--oscPath', help='Osc path', default='/gpioOSC')
parser.add_argument('-i','--OscInputPort', help='Osc input Port ', default='8000', type=int)
parser.add_argument('-tp','--TelnetOutputPort', help='Telnet Output Port ', default='7356', type=int)
parser.add_argument('-ta','--TelnetOutputAddress', help='Telnet Output address ', default='127.0.0.1')


args = parser.parse_args()

print "OSC2Telnet"

server = OSCServer( ("0.0.0.0", args.OscInputPort) )
# client = OSCClient()
# client.connect( ("127.0.0.1", 9000) )

tn = telnetlib.Telnet()
tn.open(args.TelnetOutputAddress, port=args.TelnetOutputPort)

print "Connected :: waiting for input"

def handle_timeout(self):
    sleep(.0001)

server.handle_timeout = types.MethodType(handle_timeout, server)

# def fader_callback(path, tags, args, source):
# 	print ("path", path)
# 	print ("args", args)
# 	print ("source", source)


def postTelnet(path, tags, args, source):
    tn.write (("{0} {1}".format(args[0], args[1])).encode('latin-1'))
    print(("{0} {1}".format(args[0], args[1])).encode('latin-1'))


# server.addMsgHandler( "/1/fader1",fader_callback)

server.addMsgHandler( "/telnet",postTelnet)

try:
    while True:
	       server.handle_request()
except KeyboardInterrupt:
    server.close()
