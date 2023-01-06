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
import pyautogui as pag

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI

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

while True:
    print("按下Ctrl + C 结束程序")
    # pag.position()返回鼠标的坐标
    x, y = pag.position()
    m = str(x).rjust(4)
    n = str(y).rjust(4)
    mm = round(400.0 / 1440.0 * x) + 200
    nn = - round(400.0 / 900.0 * y)
    # posStr = "当前鼠标位置:" + str(x).rjust(4) + ',' + str(y).rjust(4)
    # 打印当前鼠标位置坐标
    # print(posStr)
    # print(mm)
    # print(nn)
    # time.sleep(1)

    # 清除屏幕
    os.system('cls')


    arm = XArmAPI(ip, is_radian=True)
    arm.motion_enable(enable=True)
    arm.set_mode(0)
    arm.set_state(state=0)

    #arm.reset(wait=True)
    arm.set_position(x=mm, y=nn, z=120, roll=-180, pitch=0, yaw=0, speed=600, is_radian=False, wait=True)
    print(arm.get_position(), arm.get_position(is_radian=False))
    '''
    arm.set_position(x=300, y=200, z=250, roll=-180, pitch=0, yaw=0, speed=200, is_radian=False, wait=True)
    print(arm.get_position(), arm.get_position(is_radian=False))
    arm.set_position(x=500, y=200, z=150, roll=-180, pitch=0, yaw=0, speed=300, is_radian=False, wait=True)
    print(arm.get_position(), arm.get_position(is_radian=False))
    arm.set_position(x=500, y=-200, z=250, roll=-180, pitch=0, yaw=0, speed=400, is_radian=False, wait=True)
    print(arm.get_position(), arm.get_position(is_radian=False))
    arm.set_position(x=300, y=-200, z=150, roll=-180, pitch=0, yaw=0, speed=500, is_radian=False, wait=True)
    print(arm.get_position(), arm.get_position(is_radian=False))
    arm.set_position(x=300, y=0, z=250, roll=-180, pitch=0, yaw=0, speed=600, is_radian=False, wait=True)
    print(arm.get_position(), arm.get_position(is_radian=False))
    '''
    # arm.reset(wait=True)
    '''
    arm.set_position(x=300, y=0, z=150, roll=-3.1415926, pitch=0, yaw=0, speed=100, wait=True)
    print(arm.get_position(), arm.get_position(is_radian=False))
    arm.set_position(x=300, y=200, z=250, roll=-3.1415926, pitch=0, yaw=0, speed=200, wait=True)
    print(arm.get_position(), arm.get_position(is_radian=False))
    arm.set_position(x=500, y=200, z=150, roll=-3.1415926, pitch=0, yaw=0, speed=300, wait=True)
    print(arm.get_position(), arm.get_position(is_radian=False))
    arm.set_position(x=500, y=-200, z=250, roll=-3.1415926, pitch=0, yaw=0, speed=400, wait=True)
    print(arm.get_position(), arm.get_position(is_radian=False))
    arm.set_position(x=300, y=-200, z=150, roll=-3.1415926, pitch=0, yaw=0, speed=500, wait=True)
    print(arm.get_position(), arm.get_position(is_radian=False))
    arm.set_position(x=300, y=0, z=250, roll=-3.1415926, pitch=0, yaw=0, speed=600, wait=True)
    print(arm.get_position(), arm.get_position(is_radian=False))
    '''
    # arm.reset(wait=True)
    arm.disconnect()
