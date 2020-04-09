# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:59:01 2019

@author: ZhangJ3
"""

import serial
import time

ser = serial.Serial()
ser.port = 'COM7'
ser.baudrate = 115200
ser.bytesize = 8
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_TWO
ser.timeout = 1

ser.open()

if ser.isOpen():
    print("Open success")   
#    print(ser)
else:
    print("Open failed")    
#ser.close()   
# 
#ser.open()

ser.write('\r'.encode())

strIrate = 'irate 20 ul/min' + '\r' + '\n'

ser.write(strIrate.encode())

strRead = []
strRead = ser.readlines()

print(*strRead, sep='\n')

#strRun = 'run' + '\r' + '\n'
#
#ser.write(strRun.encode())
#print('run')

#ser.close()
#
#ser.open()
#
#time.sleep(5)
#
#strStop = 'stp' + '\r' + '\n'
#
#ser.write(strStop.encode())
#print('stop')


ser.close()