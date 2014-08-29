import Device
import time
import os

leo = Device.Device()
dev = leo.getDevice("/dev/ttyACM0")
print dev

limit = 1.7
samplesPerSec = 2

while True:
    #switch = 0
    #if switch == 0:
        #leo.readSerialOnce(dev)
    leo.writeCharViaSerial(dev, "1")
    value = []
    for each in range(0,5):
        value.append(float(leo.readSerialOnce(dev)) * 5.0/1023.0)
    #    print leo.readSerialOnce(dev)

     #   print value
        #exec(clear)
        time.sleep(1.0/samplesPerSec)
        #value = float(value)
        #voltage = value * float(5.0/1023.0)
        #if voltage > limit:
        #    leo.writeCharViaSerial(dev, "8")
        #else:
        #    leo.writeCharViaSerial(dev, "7")

        #print voltage

#    leo.writeCharViaSerial(dev, "5")
#    value = dev.readline().strip('\r')
#
#    if value != "13_on\r\n" and value != "13_off\r\n":
#        value = int(value) * (5/1023.0)
#        print value
#
#        if value > 2.4:
#            leo.writeCharViaSerial(dev, "8")
#        else:
#            leo.writeCharViaSerial(dev, "7")
#    else:
#        print value
#
#    dev.flushOutput()
