import time
import serial
arduinoData=serial.Serial('/dev/cu.usbmodem11301',115200)
time.sleep(1)
while (True):
    while (arduinoData.inWaiting()==0):
        pass
    dataPacket = arduinoData.readline() #reply
    dataPacket=str(dataPacket,'utf-8')
    # print(dataPacket)
    splitPacket=dataPacket.split(",")
    # print (splitPacket)
    i=int(splitPacket[0])
    x=int(splitPacket[1])
    y=int(splitPacket[2])
    print ("i=",i," X=",x," Y=",y)
