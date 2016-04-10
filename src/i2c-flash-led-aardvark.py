#!/bin/env python
# adapted from aai2c_eeprom.py
# PJ, 06-Jan-2013
#
# Example transcript for PIC16F1825 (device id 0x51):
# $ python i2c-flash-led-aardvark.py 
# Bitrate set to 100 kHz
# Bus lock timeout set to 150 ms
# count= 10 data_in= array('B', [0, 1, 2, 3, 4, 5, 6, 7, 0, 1])
#
# For FlashForth slave implementation (device id 0x52),
# we have counting numbers (from 1) and lots of them...

import sys
from aardvark_py import *

handle = aa_open(0)
if (handle <= 0):
    print "Unable to open Aardvark device on port %d" % port
    print "Error code = %d" % handle
    sys.exit()
aa_configure(handle,  AA_CONFIG_SPI_I2C)
# Set the bitrate to 100kHz
bitrate = aa_i2c_bitrate(handle, 100)
print "Bitrate set to %d kHz" % bitrate
# Set the bus lock timeout 150ms
bus_timeout = aa_i2c_bus_timeout(handle, 150)
print "Bus lock timeout set to %d ms" % bus_timeout
device = 0x52
if 1:
    # Turn on the LED and off again.
    aa_i2c_write(handle, device, AA_I2C_NO_FLAGS, array('B',[0x01]))
    aa_sleep_ms(200)
    aa_i2c_write(handle, device, AA_I2C_NO_FLAGS, array('B',[0x00]))
if 1:
    # Read bytes from slave.
    length = 200
    (count, data_in) = aa_i2c_read(handle, device, AA_I2C_NO_FLAGS, length)
    print "count=", count, "data_in=", data_in
    if (count < 0):
        print "error: %s" % aa_status_string(count)
    elif (count == 0):
        print "error: no bytes read"
        print "  are you sure you have the right slave address?"
    elif (count != length):
        print "error: read %d bytes (expected %d)" % (count, length)
aa_close(handle)
