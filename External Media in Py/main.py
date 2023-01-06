import os, time

import pyautogui as pag
# import required module
from playsound import playsound

try:
    while True:
        print("按下Ctrl + C 结束程序")
        # pag.position()返回鼠标的坐标
        x, y = pag.position()
        m = str(x).rjust(4)
        n = str(y).rjust(4)
        mm = round(400.0/1440.0 * x)
        nn = round(400.0/900.0 * y)
        posStr = "当前鼠标位置:" + str(x).rjust(4) + ',' + str(y).rjust(4)
        # 打印当前鼠标位置坐标
        print(posStr)
        print(mm)
        print(nn)
        time.sleep(5)

        # for playing note.wav file
        playsound('/Users/toto/PycharmProjects/MousePos/fa-78409 copy.mp3')
        print('playing sound using  playsound')

        # 清除屏幕
        os.system('cls')
# 捕获异常 KeyboardInterrupt:用户中断执行(通常是输入^C)
except KeyboardInterrupt:
    print('已退出')