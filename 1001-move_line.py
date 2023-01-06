#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2019, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

"""
Description: Move line(linear motion)
"""

import os
import sys
import time
import serial

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI
# import required module
from playsound import playsound

#######################################################
"""
Just for test example
"""
if len(sys.argv) >= 2:
    ip = sys.argv[1]
else:
    try:
        from configparser import ConfigParser

        parser = ConfigParser()
        parser.read('../robot.conf')
        ip = parser.get('xArm', 'ip')
    except:
        ip = input('Please input the xArm ip address:')
        if not ip:
            print('input error, exit')
            sys.exit(1)
########################################################
# play sound all
playsound('/Users/toto/Desktop/xArm-Python-SDK-master/example/wrapper/common/media/do-sound1.mp3')
playsound('/Users/toto/Desktop/xArm-Python-SDK-master/example/wrapper/common/media/fa-sound2.mp3')
playsound('/Users/toto/Desktop/xArm-Python-SDK-master/example/wrapper/common/media/la-sound3.mp3')
#  playsound('/Users/toto/Desktop/xArm-Python-SDK-master/example/wrapper/common/media/glad-piano-logo.mp3')
########################################################
arm = XArmAPI(ip)
arm.motion_enable(enable=True)

while 1:
    arduinoData = serial.Serial('/dev/cu.usbmodem1401', 115200)
    # time.sleep(1)
    while (arduinoData.inWaiting() == 0):
        pass
    dataPacket = arduinoData.readline()  # reply
    dataPacket = str(dataPacket, 'utf-8')
    print(dataPacket)
    splitPacket = dataPacket.split(",")
    print (splitPacket)
    noteNum = int(splitPacket[0])
    noteX = int(splitPacket[1])
    noteY = int(splitPacket[2])
    print("i=", noteNum, " X=", noteX, " Y=", noteY)
    ##################################################
    if noteNum == 1 or noteNum == 2 or noteNum == 3:
        playsound('/Users/toto/Desktop/xArm-Python-SDK-master/example/wrapper/common/media/error.mp3')
        print('#### WAIT, LET ME HELP YOU ####')
        #arm = XArmAPI(ip)
        #arm.motion_enable(enable=True)

        # arm.set_mode(0)
        # arm.set_state(state=0)
        # arm.reset(wait=True)

        # initial position
        arm.set_position(x=241, y=0, z=451, roll=-180, pitch=0, yaw=0, speed=100, wait=True)

        # open gripper
        arm.set_gripper_enable(True)
        arm.set_gripper_mode(0)
        code = arm.set_gripper_position(650, speed=2000, auto_enable=True)

        arm.set_position(x=(noteX - 30), y=(noteY - 10), z=215, roll=-180, pitch=0, yaw=0, speed=100, wait=True)
        # close gripper feed back
        code = arm.set_gripper_position(320, speed=2000, auto_enable=True)

        arm.set_position(x=(noteX - 30), y=(noteY - 10), z=450, roll=-180, pitch=0, yaw=0, speed=100, wait=True)

        if noteNum == 1:
            arm.set_position(x=275, y=noteY, z=215, roll=-180, pitch=0, yaw=0, speed=100, wait=True)
            print(arm.get_position(), arm.get_position(is_radian=True))
            playsound('/Users/toto/Desktop/xArm-Python-SDK-master/example/wrapper/common/media/do-sound1.mp3')
        elif noteNum == 2:
            arm.set_position(x=380, y=noteY, z=215, roll=-180, pitch=0, yaw=0, speed=100, wait=True)
            print(arm.get_position(), arm.get_position(is_radian=True))
            playsound('/Users/toto/Desktop/xArm-Python-SDK-master/example/wrapper/common/media/fa-sound2.mp3')
        elif noteNum == 3:
            arm.set_position(x=190, y=noteY, z=215, roll=-180, pitch=0, yaw=0, speed=100, wait=True)
            print(arm.get_position(), arm.get_position(is_radian=True))
            playsound('/Users/toto/Desktop/xArm-Python-SDK-master/example/wrapper/common/media/la-sound3.mp3')
            playsound('/Users/toto/Desktop/xArm-Python-SDK-master/example/wrapper/common/media/glad-piano-logo.mp3')
        else:
            print('error')

        # open gripper
        code = arm.set_gripper_position(600, speed=2000, auto_enable=True)

        # initial position
        arm.set_position(x=241, y=0, z=451, roll=-180, pitch=0, yaw=0, speed=100)

        # arm.reset(wait=True)
        #arm.disconnect()

        ##################################################
    else:
        print('#### PLEASE CONTINUE ####')
        #arm = XArmAPI(ip)
        #arm.motion_enable(enable=True)
        # initial position
        #arm.set_position(x=241, y=0, z=451, roll=-180, pitch=0, yaw=0, speed=100, wait=True)
        arm.set_position(x=241, y=0, z=451, roll=-180, pitch=0, yaw=0, speed=100)
        arm.set_gripper_enable(True)
        arm.set_gripper_mode(0)
        #code = arm.set_gripper_position(600, wait=True, speed=2000, auto_enable=True)
        code = arm.set_gripper_position(650, speed=2000, auto_enable=True)

        # Play sound
        if noteNum == 11: playsound('/Users/toto/Desktop/xArm-Python-SDK-master/example/wrapper/common/media/do-sound1.mp3')
        elif noteNum == 12: playsound('/Users/toto/Desktop/xArm-Python-SDK-master/example/wrapper/common/media/fa-sound2.mp3')
        elif noteNum == 13: playsound('/Users/toto/Desktop/xArm-Python-SDK-master/example/wrapper/common/media/la-sound3.mp3')
        else: print('please continue?')

arm.disconnect()