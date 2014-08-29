import Device
import time

leo = Device.Device()
dev = leo.getDevice("/dev/ttyACM0")

while True:
    leo.writeCharViaSerial(dev, "8")
    time.sleep(0.06)
    leo.writeCharViaSerial(dev, "7")
    time.sleep(0.06)
#    leo.writeCharViaSerial(dev, "8")
#    time.sleep(0.12)
#    leo.writeCharViaSerial(dev, "7")
#    time.sleep(0.12)
#    leo.writeCharViaSerial(dev,"8")
#    time.sleep(0.24)
#    leo.writeCharViaSerial(dev, "7")
#    time.sleep(0.24)
#    leo.writeCharViaSerial(dev, "8")
#    time.sleep(0.1)
#    leo.writeCharViaSerial(dev, "7")
#    time.sleep(0.1)

    
